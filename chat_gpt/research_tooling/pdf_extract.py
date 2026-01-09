import subprocess
from pathlib import Path
from typing import Optional

def extract_text_pymupdf(pdf_path: Path) -> Optional[str]:
    try:
        import fitz  # type: ignore
    except Exception:
        return None

    doc = fitz.open(pdf_path)
    parts: list[str] = []
    for i in range(len(doc)):
        page = doc.load_page(i)
        parts.append(f"\n\n---\n\n# Page {i + 1}\n\n")
        parts.append(page.get_text("text"))
    return "".join(parts)


def extract_text_pypdf(pdf_path: Path) -> Optional[str]:
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        return None

    reader = PdfReader(str(pdf_path))
    parts: list[str] = []
    for i, page in enumerate(reader.pages):
        parts.append(f"\n\n---\n\n# Page {i + 1}\n\n")
        parts.append(page.extract_text() or "")
    return "".join(parts)


def extract_text_pdftotext(pdf_path: Path) -> Optional[str]:
    try:
        subprocess.run(["pdftotext", "-v"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    except FileNotFoundError:
        return None

    proc = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(pdf_path), "-"],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return None
    return proc.stdout


def extract_pdf_text(pdf_path: Path) -> str:
    for extractor in (extract_text_pymupdf, extract_text_pypdf, extract_text_pdftotext):
        text = extractor(pdf_path)
        if text and text.strip():
            return text

    raise RuntimeError(
        "Falha ao extrair texto do PDF. Instale uma das opções:\n"
        "- PyMuPDF (recomendado): pip install pymupdf\n"
        "- pypdf: pip install pypdf\n"
        "Ou instale o binário 'pdftotext' (poppler-utils) no sistema."
    )
