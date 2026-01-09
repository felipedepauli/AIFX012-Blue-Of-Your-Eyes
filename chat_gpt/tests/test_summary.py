import pytest
from unittest.mock import patch
from chat_gpt.research_tooling.cli import main
from chat_gpt.research_tooling.paths import build_paths

def test_summary_generation(tmp_path):
    """
    Test that --summary aggregates data from 00_metadata.md and triage_report.md
    into candidates_summary.md
    """
    project_root = tmp_path / "projects" / "test_proj"
    project_root.mkdir(parents=True)
    
    # Needs docs dir for cli to be happy? No, --summary short-circuits.
    
    # Create fake processed papers in project_root/pdf
    pdf_dir = project_root / "pdf"
    pdf_dir.mkdir()
    
    # Paper 1: Complete
    p1 = pdf_dir / "paper1"
    p1.mkdir()
    (p1 / "00_metadata.md").write_text("- Título: Paper One\n- Status: triagem\n", encoding="utf-8")
    (p1 / "triage_report.md").write_text("""
        # Triage Report: Paper One
        ## Relevância (0-3)
        [x] 3 - Alta
        ## Decisão
        - [x] Candidato
        ## Tags
        - #ai
        - #vision
    """, encoding="utf-8")
    
    # Paper 2: Missing Triage
    p2 = pdf_dir / "paper2"
    p2.mkdir()
    (p2 / "00_metadata.md").write_text("- Título: Paper Two\n- Status: lido-1a-passada\n", encoding="utf-8")
    
    # Run CLI with --summary
    with patch("pathlib.Path.cwd", return_value=tmp_path):
        argv = ["--project", "test_proj", "--summary"]
        ret = main(argv)
        assert ret == 0
        
    summary_file = project_root / "candidates_summary.md"
    assert summary_file.exists()
    
    content = summary_file.read_text(encoding="utf-8")
    assert "# Candidates Summary" in content
    
    # Check Paper 1 row
    assert "Paper One" in content
    assert "triagem" in content
    assert "3" in content # Relevance
    assert "Candidato" in content
    assert "#ai, #vision" in content
    
    # Check Paper 2 row
    assert "Paper Two" in content
    assert "lido-1a-passada" in content
    assert "-" in content # Missing relevance
