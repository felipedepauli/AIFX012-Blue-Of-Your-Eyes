# Backlog

## Sprint 0 — Harden do que já existe
1) Refatorar pdf_runner.py em módulos (sem mudar comportamento)
2) Adicionar smoke tests
3) Validar contratos de metadata/status

## Sprint 1 — Etapa de triagem automatizada (sem web)
1) Gerar `triage_report.md` por paper (template + placeholders)
2) Gerar `candidates_summary.md` agregado

## Sprint 2 — Execução Automatizada (LLM Integration)
1) Setup de Dependências (`langchain`, `openai`, `python-dotenv`) e Chaves API.
2) Criar módulo `llm_client.py` (wrapper simples para chamadas).
3) Implementar comando `--auto-run` no runner para executar o passo atual usando o LLM.
