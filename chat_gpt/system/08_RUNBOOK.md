# Runbook

## Rodar em um PDF
python3 chat_gpt/scripts/pdf_runner.py --pdf chat_gpt/scripts/docs/foo.pdf --objective "..." --interactive-steps --print-prompt

## Rodar em batch
python3 chat_gpt/scripts/pdf_runner.py --all --no-interactive

## Problemas comuns
- Texto vazio -> instalar pymupdf / pypdf / pdftotext
- PDF com imagem -> (futuro) OCR opcional
