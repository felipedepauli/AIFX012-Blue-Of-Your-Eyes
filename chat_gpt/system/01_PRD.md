# PRD — Literature Review Pipeline (Markdown-first)

## Problema
Revisão de literatura é lenta e difícil de rastrear. Queremos um pipeline que transforme PDFs em um conjunto de artefatos Markdown consistentes, e possibilite uso de IA para triagem, leitura em camadas e síntese.

## Usuário-alvo
Pesquisador/engenheiro produzindo "Related Work", decisão de implementação, ou fundamentação técnica.

## Entradas
- PDFs em `chat_gpt/docs/*.pdf`
- Objetivo de leitura (string)
- Configuração (max_step, criticidade, tags, status)

## Saídas (por paper)
Tudo dentro de um diretório `chat_gpt/reviews/{slug}`
- `paper_text.md` extraído
- `00_metadata.md` com status
- `01_first_pass.md`, `02_second_pass.md`, `03_third_pass.md`
- `04_references_to_read.md`
- `05_ideas_future_work.md`
- `README.md` do paper

## Requisitos funcionais
- Preparar estrutura por paper (slug) de forma idempotente
- Controlar progressão por status
- Gerar prompts por etapa (para LLM) com referências aos arquivos
- Permitir batch (todos PDFs) e single
- Registrar logs e falhas de extração de texto com fallback

## Requisitos não-funcionais
- Execução determinística
- Sem “conteúdo mágico”: tudo versionado em Markdown
- Baixo acoplamento entre extração, templates e orquestração
- Fácil de testar (unit + smoke)

## Fora de escopo (por enquanto)
- Buscar papers na web
- Gerar citações BibTeX automaticamente
- Interface web (somente CLI)
