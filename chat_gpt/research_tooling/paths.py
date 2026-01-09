import unicodedata
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass(frozen=True)
class PaperPaths:
    slug: str
    out_dir: Path
    metadata: Path
    first_pass: Path
    second_pass: Path
    third_pass: Path
    references: Path
    ideas: Path
    readme: Path
    extracted_text: Path
    prompt_step1: Path
    prompt_step2: Path
    prompt_step3: Path
    prompt_step4: Path
    prompt_step5: Path
    triage_report: Path


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "paper"


def build_paths(output_root: Path, slug: str) -> PaperPaths:
    out_dir = output_root / slug
    return PaperPaths(
        slug=slug,
        out_dir=out_dir,
        metadata=out_dir / "00_metadata.md",
        first_pass=out_dir / "01_first_pass.md",
        second_pass=out_dir / "02_second_pass.md",
        third_pass=out_dir / "03_third_pass.md",
        references=out_dir / "04_references_to_read.md",
        ideas=out_dir / "05_ideas_future_work.md",
        triage_report=out_dir / "triage_report.md",
        readme=out_dir / "README.md",
        extracted_text=out_dir / "paper_text.md",
        prompt_step1=out_dir / "prompt_step1.md",
        prompt_step2=out_dir / "prompt_step2.md",
        prompt_step3=out_dir / "prompt_step3.md",
        prompt_step4=out_dir / "prompt_step4_references.md",
        prompt_step5=out_dir / "prompt_step5_ideas.md",
    )


def read_text_file(path: Path) -> Optional[str]:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8")
    return True
