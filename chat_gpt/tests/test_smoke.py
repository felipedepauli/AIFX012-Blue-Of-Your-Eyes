import pytest
from unittest.mock import patch, MagicMock
from chat_gpt.research_tooling.cli import main
from pathlib import Path
import sys

def test_help_command(capsys):
    """Smoke test: Ensure --help runs without error."""
    with pytest.raises(SystemExit) as exc:
        main(["--help"])
    assert exc.value.code == 0
    
    captured = capsys.readouterr()
    assert "usage: " in captured.out or "usage: " in captured.err

@patch("chat_gpt.research_tooling.cli.extract_pdf_text")
def test_prepare_single_paper_flow(mock_extract, repo_root_path, tmp_path):
    """
    Test end-to-end flow for a single PDF.
    Mocks PDF extraction to avoid needing a real PDF parser or file.
    """
    mock_extract.return_value = "Conteúdo extraído do dummy PDF."

    # Setup fake input PDF
    input_dir = tmp_path / "research" / "docs"
    input_dir.mkdir(parents=True)
    pdf_file = input_dir / "paper.pdf"
    pdf_file.write_bytes(b"%PDF-dummy")

    # Setup fake methodology.md because cli checks for it
    methodology = repo_root_path / "research" / "methodology.md"
    # Ensure it exists or mock read_text_file? 
    # cli.py reads it using read_text_file from paths.py which essentially uses Path.read_text
    # But cli.py tries to find it. 
    # For correctness in test environment, let's assume the real file exists in the repo.
    # If not, we'd need to mock read_text_file or ensure the file is there. 
    # The repo_root_path fixture points to actual repo, so it should exist if the repo is healthy.
    if not methodology.exists():
         pytest.skip("research/methodology.md not found in repo, skipping integration test requiring it.")

    # Output dir in tmp
    output_root = tmp_path / "research" / "pdf"

    argv = [
        "--pdf", str(pdf_file),
        "--output-root", str(output_root),
        "--objective", "smoke test",
        "--max-step", "1",
        "--criticality", "baixo",
        "--no-interactive"
    ]

    ret = main(argv)
    assert ret == 0

    # Verify artifacts
    slug_dir = output_root / "paper"
    assert (slug_dir / "00_metadata.md").exists()
    assert (slug_dir / "paper_text.md").exists()
    assert (slug_dir / "prompt_step1.md").exists()
    
    # Check content of paper_text
    assert "Conteúdo extraído" in (slug_dir / "paper_text.md").read_text(encoding="utf-8")

@patch("chat_gpt.research_tooling.cli.extract_pdf_text")
def test_project_argument_resolution(mock_extract, repo_root_path, tmp_path):
    """
    Test if --project correctly redirects inputs and outputs.
    """
    mock_extract.return_value = "Project PDF Content"

    # Simulate project structure in tmp_path to avoid writing to real repo
    # But cli.py resolves --project relative to CWD.
    # We need to change CWD or mock Path.cwd()
    
    with patch("pathlib.Path.cwd", return_value=tmp_path):
        project_name = "myproj"
        proj_dir = tmp_path / "projects" / project_name
        docs_dir = proj_dir / "docs"
        docs_dir.mkdir(parents=True)
        
        pdf_file = docs_dir / "proj_paper.pdf"
        pdf_file.write_bytes(b"dummy")

        # We also need methodology.md to be findable. 
        # cli.py looks in repo_root/research/methodology.md
        # since we mocked cwd to tmp_path, repo_root is now tmp_path.
        # So we must create methodology.md in tmp_path/research/methodology.md
        (tmp_path / "research").mkdir()
        (tmp_path / "research" / "methodology.md").write_text("System Prompt Dummy")

        argv = [
            "--project", project_name,
            "--pdf", str(pdf_file),
            "--objective", "proj test",
            "--no-interactive"
        ]

        # Note on --pdf argument: in cli.py, if we provide full path to --pdf, it uses it.
        # The --project arg mainly sets default docs_dir and output_root.
        # output_root should be proj_dir / "pdf"
        
        ret = main(argv)
        assert ret == 0

        output_root = proj_dir / "pdf"
        slug_dir = output_root / "proj-paper"
        
        assert slug_dir.exists()
        assert (slug_dir / "00_metadata.md").exists()
