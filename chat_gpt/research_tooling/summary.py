import re
from pathlib import Path
from typing import List, Dict, Optional
from .paths import read_text_file

def parse_metadata(content: str) -> Dict[str, str]:
    data = {}
    # Extract Title
    title_match = re.search(r"^\s*-\s*Título\s*:\s*(.+)$", content, re.MULTILINE | re.IGNORECASE)
    if title_match:
        data["title"] = title_match.group(1).strip()
    
    # Extract Status - reuse logic from status.py roughly or just regex here
    status_match = re.search(r"^\s*-\s*Status\s*:\s*(.+)$", content, re.MULTILINE | re.IGNORECASE)
    if status_match:
        data["status"] = status_match.group(1).strip()
        
    return data

def parse_triage(content: str) -> Dict[str, str]:
    data = {
        "relevance": "-",
        "decision": "-",
        "tags": []
    }
    
    # Relevance: [x] N - ...
    rel_match = re.search(r"^\s*\[[xX]\]\s*(\d)\s*-", content, re.MULTILINE)
    if rel_match:
        data["relevance"] = rel_match.group(1)
        
    # Decision: - [x] Decision
    dec_match = re.search(r"^\s*-\s*\[[xX]\]\s*(Candidato|Arquivado)", content, re.MULTILINE | re.IGNORECASE)
    if dec_match:
        data["decision"] = dec_match.group(1)
        
    # Tags: - #tag
    tags = re.findall(r"^\s*-\s*(#\w[\w-]*)", content, re.MULTILINE)
    if tags:
        data["tags"] = ", ".join(tags)
    else:
        data["tags"] = "-"
        
    return data

def generate_summary_table(rows: List[Dict[str, str]]) -> str:
    # Header
    md = "| Título | Status | Relevância | Decisão | Tags | Slug |\n"
    md += "| --- | --- | :---: | --- | --- | --- |\n"
    
    for row in rows:
        title = row.get("title", "Unknown").replace("|", "-")
        status = row.get("status", "-")
        relevance = row.get("relevance", "-")
        decision = row.get("decision", "-")
        tags = row.get("tags", "-")
        slug = row.get("slug", "")
        
        md += f"| {title} | {status} | {relevance} | {decision} | {tags} | {slug} |\n"
        
    return md

def generate_summary(output_root: Path, project_root: Path) -> Path:
    """
    Aggregates metadata and triage reports from output_root (where PDF folders are)
    and writes a summary to project_root/candidates_summary.md.
    """
    rows = []
    
    if not output_root.exists():
        print(f"Diretório de saída não encontrado: {output_root}")
        return project_root / "candidates_summary.md"

    # Iterate over paper directories
    for paper_dir in sorted(output_root.iterdir()):
        if not paper_dir.is_dir():
            continue
            
        slug = paper_dir.name
        metadata_path = paper_dir / "00_metadata.md"
        triage_path = paper_dir / "triage_report.md"
        
        row = {"slug": slug, "title": slug} # Default title is slug
        
        # Parse Metadata
        if metadata_path.exists():
            meta_content = read_text_file(metadata_path)
            if meta_content:
                row.update(parse_metadata(meta_content))
        
        # Parse Triage
        if triage_path.exists():
            triage_content = read_text_file(triage_path)
            if triage_content:
                row.update(parse_triage(triage_content))
        
        rows.append(row)
        
    # Generate Markdown
    table_md = generate_summary_table(rows)
    
    final_md = f"# Candidates Summary\n\nTotal Papers: {len(rows)}\n\n{table_md}"
    
    summary_path = project_root / "candidates_summary.md"
    summary_path.write_text(final_md, encoding="utf-8")
    
    print(f"[ok] Resumo gerado em: {summary_path}")
    return summary_path
