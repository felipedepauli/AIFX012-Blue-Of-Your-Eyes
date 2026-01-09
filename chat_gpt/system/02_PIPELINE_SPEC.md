# Pipeline Spec

## Status do paper
- triagem
- lido-1a-passada
- lido-2a-passada
- lido-3a-passada
- arquivado (descartado)
- candidato (prioritário)

## Etapas (blocos)
### A) Ingestão
Entrada: PDF
Saída: `paper_text.md`, `00_metadata.md` inicial

### B) Triagem
Entrada: abstract/intro/conclusão (do texto extraído)
Saída: decisão: arquivar/candidato + tags + resumo 5P

### C) Leitura em camadas
Passo 1: visão geral + arquitetura + 5P + estrutura do documento (títulos e subtítulos)
Passo 2: método/figuras/resultados + limitações
Passo 3: reconstrução mental + suposições + ideias futuras

### D) Extração de evidências
Produzir bullets com "afirmação -> evidência (seção/página)"

### E) Síntese temática
Agrupar papers por tema e produzir outline para Related Work

### F) Escrita
Gerar rascunhos Markdown com seções e “to-dos” de validação
