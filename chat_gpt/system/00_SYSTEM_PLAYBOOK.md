# System Playbook (Contrato de Trabalho)

## Objetivo
Construir um pipeline de revisão de literatura com IA, orientado a arquivos Markdown e extração de PDF, com rastreabilidade por status.

## Modo de execução (SEMPRE)
Para cada etapa:
1) Você implementa APENAS o escopo da etapa.
2) Você explica:
   - o que criou/alterou
   - por que escolheu esse design
   - como testar (comandos exatos)
   - quais arquivos foram modificados
3) Você PARA e pergunta: "Valida? (sim/não)". Só continua após validação.

## Regras
- Não mudar interfaces existentes sem atualizar o DATA_CONTRACTS e o RUNBOOK.
- Não adicionar dependências sem justificar (benefício + custo + alternativa).
- Não fazer “big bang refactor”. Entregas pequenas e testáveis.
- Toda saída gerada (arquivos do pipeline) deve ser determinística e reexecutável.

## Definição de Pronto (DoD) mínima por etapa
- CLI roda sem erro
- Gera os arquivos esperados
- Testes básicos passam
- Documentação atualizada
