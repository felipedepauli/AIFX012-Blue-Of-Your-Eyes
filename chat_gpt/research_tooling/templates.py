import textwrap
from pathlib import Path

def make_metadata_template(pdf_path: Path, title_guess: str) -> str:
    return textwrap.dedent(
        f"""\
        # Metadata

        - Source PDF: `{pdf_path}`
        - Título: {title_guess}
        - Autores:
        - Ano:
        - Venue:
        - DOI/URL:
        - Tags: 
        - Status: triagem
        """
    )


def make_pass_template(title: str) -> str:
    return textwrap.dedent(
        f"""\
        # {title}

        """
    )


def make_readme_template(slug: str) -> str:
    return textwrap.dedent(
        f"""\
        # Paper: `{slug}`

        - `00_metadata.md`
        - `01_first_pass.md`
        - `02_second_pass.md`
        - `03_third_pass.md`
        - `04_references_to_read.md`
        - `05_ideas_future_work.md`
        - `paper_text.md`
        """
    )


def make_triage_template(title_guess: str) -> str:
    return textwrap.dedent(
        f"""\
        # Triage Report: {title_guess}

        ## Relevância (0-3)
        [ ] 0 - Irrelevante
        [ ] 1 - Baixa
        [ ] 2 - Média
        [ ] 3 - Alta

        ## Motivos
        - Motivo 1
        - Motivo 2
        - Motivo 3

        ## 5P Análise Rápida
        - **Problem**: 
        - **Platform/Context**: 
        - **Proposal/Solution**: 
        - **Proof/Validation**: 
        - **Product/Contribution**: 

        ## Decisão
        - [ ] Candidato (Avançar para Passo 1)
        - [ ] Arquivado (Não ler mais)

        ## Tags
        - #tag1
        - #tag2
        """
    )
