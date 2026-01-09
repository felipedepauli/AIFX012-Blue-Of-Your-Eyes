# Architecture

## Objetivo
Separar:
- extração de texto (PDF -> MD)
- estrutura de artefatos (folders/files)
- geração de prompts
- status/progressão
- (futuro) execução de LLM/RAG

## Módulos sugeridos
- `research_tooling/pdf_extract.py`
- `research_tooling/paths.py`
- `research_tooling/status.py`
- `research_tooling/templates.py`
- `research_tooling/prompts.py`
- `research_tooling/cli.py`

## Contratos
- Nenhum módulo escreve fora do `output_root/<slug>/`
- Status é fonte de verdade para "próximo passo"
- Templates são puros (string in -> string out)
