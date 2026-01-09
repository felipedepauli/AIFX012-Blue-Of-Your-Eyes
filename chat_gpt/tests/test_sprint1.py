import pytest
from unittest.mock import patch, MagicMock
from chat_gpt.research_tooling.cli import main
from pathlib import Path

@patch("chat_gpt.research_tooling.cli.extract_pdf_text")
def test_triage_report_creation(mock_extract, repo_root_path, tmp_path):
    """
    Sprint 1 verification: Ensure triage_report.md is created during prepare_paper.
    """
    mock_extract.return_value = "Content"
    
    # Setup inputs
    input_dir = tmp_path / "research" / "docs"
    input_dir.mkdir(parents=True)
    pdf_file = input_dir / "triage_test.pdf"
    pdf_file.write_bytes(b"dummy")

    # Setup methodology
    if not (repo_root_path / "research" / "methodology.md").exists():
        pytest.skip("Methodology not found")

    output_root = tmp_path / "research" / "pdf"

    argv = [
        "--pdf", str(pdf_file),
        "--output-root", str(output_root),
        "--objective", "triage test",
        "--no-interactive"
    ]

    ret = main(argv)
    assert ret == 0

    slug_dir = output_root / "triage-test"
    triage_file = slug_dir / "triage_report.md"
    
    assert triage_file.exists(), "triage_report.md should be created"
    content = triage_file.read_text(encoding="utf-8")
    assert "# Triage Report:" in content
    assert "## Relevância" in content
    assert "## 5P Análise Rápida" in content
