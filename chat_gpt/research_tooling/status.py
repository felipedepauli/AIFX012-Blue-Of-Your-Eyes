import re
from pathlib import Path
from typing import Optional
from .paths import read_text_file

STATUS_ORDER = [
    "triagem",
    "lido-1a-passada",
    "lido-2a-passada",
    "lido-3a-passada",
    "extraindo-referencias",
    "extraindo-ideias",
    "arquivado",
    "candidato",
]

STATUS_TO_NEXT_STEP = {
    "triagem": 1,
    "lido-1a-passada": 2,
    "lido-2a-passada": 3,
    "lido-3a-passada": 4,
    "extraindo-referencias": 5,
    "extraindo-ideias": None,
    "arquivado": None,
    "candidato": None,
}

def parse_status(metadata_text: str) -> str:
    match = re.search(r"^\s*-\s*Status\s*:\s*(.+?)\s*$", metadata_text, flags=re.MULTILINE)
    if not match:
        return "triagem"
    status = match.group(1).strip()
    if status not in STATUS_TO_NEXT_STEP:
        return "triagem"
    return status


def read_status(metadata_path: Path) -> str:
    text = read_text_file(metadata_path)
    if not text:
        return "triagem"
    return parse_status(text)


def set_status(metadata_path: Path, new_status: str) -> None:
    if new_status not in STATUS_TO_NEXT_STEP:
        raise ValueError(f"Status inválido: {new_status}")

    existing = read_text_file(metadata_path) or ""

    if re.search(r"^\s*-\s*Status\s*:\s*.+$", existing, flags=re.MULTILINE):
        updated = re.sub(
            r"^(\s*-\s*Status\s*:)\s*.+$",
            rf"\1 {new_status}",
            existing,
            flags=re.MULTILINE,
        )
    else:
        updated = (existing.rstrip() + "\n" if existing.strip() else "") + f"- Status: {new_status}\n"

    metadata_path.write_text(updated, encoding="utf-8")


def next_step_from_status(status: str, max_step: int) -> Optional[int]:
    step = STATUS_TO_NEXT_STEP.get(status, 1)
    if step is None:
        return None
    if step > max_step:
        return None
    return step
