# AIFX012 - The Blue of your Eyes

Este projeto fornece um **pipeline automatizado para leitura e análise de artigos científicos (PDFs)**. Ele orquestra desde a extração de texto até a análise semântica em camadas (Passos 1, 2, 3), integrando-se opcionalmente com LLMs (OpenAI) para execução autônoma.

## 1. Visão Geral

O objetivo é transformar o processo de pesquisa bibliográfica (frequentemente manual e desorganizado) em um fluxo estruturado e auditável.

**O sistema realiza:**
1.  **Ingestão**: Lê PDFs de pastas organizadas por projeto.
2.  **Triagem**: Gera relatórios de triagem para decisão rápida (Ler ou Arquivar).
3.  **Leitura em Camadas** (Three-Pass Approach):
    *   **Passo 1**: Visão geral, Abstract, Conclusão e 5Ps (Problem, Platform, Proposal, Proof, Product).
    *   **Passo 2**: Detalhes visuais e claims principais.
    *   **Passo 3**: Reproducibilidade e detalhes profundos.
4.  **Síntese**: Agrega todos os metadados em um painel único (`candidates_summary.md`).

---

## 2. O que você pode fazer (Funcionalidades)

### 📄 Preparar um Paper (Modo Manual/IA Editor)
Gera a estrutura de pastas e cria **prompts prontos** (`prompt_step1.md`, etc.) que você pode copiar e colar manualmente em um chat com IA (ChatGPT, Claude, Windsurf) para analisar o paper.

### 🤖 Executar Automaticamente (Modo Auto-Run)
Aciona o LLM (via OpenAI API) para ler o prompt gerado, processar o texto do paper e escrever o relatório de saída automaticamente, sem intervenção humana.

### 🚦 Realizar Triagem
Gera um `triage_report.md` para cada paper, onde você define se ele é um "Candidato" ou "Arquivado" antes de investir tempo lendo.

### 📊 Gerar Resumo Executivo
Cria uma tabela unificada (`candidates_summary.md`) listando todos os papers do projeto com seus status, relevância e decisões de triagem.

---

## 3. Variações e Modos de Uso

O script principal é `chat_gpt/scripts/pdf_runner.py`.

### Por Escopo
*   **Um único Paper**: `--pdf projects/reid/docs/paper.pdf`
*   **Todos do Projeto**: `--project reid --all`

### Por Interatividade
*   **Interativo (Padrão)**: Pergunta antes de avançar para o próximo passo/paper.
*   **Não-Interativo (`--no-interactive`)**: Processa tudo em lote sem pausas.
*   **Passo-a-Passo (`--interactive-steps`)**: Pausa entre Passo 1, 2 e 3 do mesmo paper para validação.

### Por Execução
*   **Geração de Prompts (Padrão)**: Apenas cria os arquivos `.md` com os comandos.
*   **Automático (`--auto-run`)**: Executa os prompts usando a API da OpenAI.
    *   Requer `--model gpt-4o` (ou outro).
    *   Requer `.env` configurado.

### Por Ação Específica
*   **Resumo (`--summary`)**: Não prepara papers, apenas varre os já existentes para gerar o relatório consolidado.

---

## 4. Arquitetura do Sistema

O sistema é modularizado dentro de `chat_gpt/research_tooling/`.

### Estrutura de Arquivos e Responsabilidades

#### 📂 `chat_gpt/research_tooling/`
*   **`cli.py`**: **Ponto de entrada**. Gerencia argumentos, orquestra o fluxo, decide se roda auto-run ou apenas gera prompts.
*   **`paths.py`**: **Gerenciador de Caminhos**. Define onde cada arquivo (PDF, md, prompt) deve ficar. Centraliza a lógica de diretórios (`projects/<nome>/pdf/...`).
*   **`prompts.py`**: **Fábrica de Prompts**. Contém os templates "inteligentes" que orientam o LLM sobre o que fazer em cada passo (Passo 1, 2, 3), injetando o contexto do paper.
*   **`templates.py`**: **Templates Estáticos**. Estruturas markdown vazias para `triage_report.md`, `00_metadata.md`, etc.
*   **`pdf_extract.py`**: **Motor de Extração**. Usa `pymupdf` (ou fallbacks) para converter PDF binário em texto limpo (`paper_text.md`).
*   **`status.py`**: **Máquina de Estado**. Lê e escreve o status no `00_metadata.md` (ex: `triagem` -> `lido-1a-passada`). Garante a consistência do fluxo.
*   **`summary.py`**: **Agregador**. Varre pastas de output e consolida dados em tabelas markdown.
*   **`llm_client.py`**: **Gateway LLM**. Wrapper em cima do LangChain/OpenAI para enviar prompts e receber respostas.

#### 📂 `projects/<project_name>/`
*   **`docs/`**: Onde você coloca os PDFs brutos.
*   **`pdf/`**: Onde o sistema gera as saídas (uma pasta por paper).
*   **`candidates_summary.md`**: O relatório consolidado do projeto.

---

## 5. Instalação e Configuração

### Pré-requisitos
*   Python 3.10+
*   Chave de API OpenAI (para modo Auto-Run)

### Instalação
1.  Clone o repositório.
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Configuração (.env)
Crie um arquivo `.env` na raiz:
```properties
OPENAI_API_KEY=sk-proj-123456...
```

---

## 6. Exemplos de Comandos

**Preparar (Triagem/Prompts) para um projeto inteiro:**
```bash
python3 chat_gpt/scripts/pdf_runner.py --project reid --all
```

**Rodar Análise Automática (Passo 1) em um paper específico:**
```bash
python3 chat_gpt/scripts/pdf_runner.py --project reid --pdf "projects/reid/docs/paper.pdf" --auto-run --model gpt-4o
```

**Gerar Painel de Resumo:**
```bash
python3 chat_gpt/scripts/pdf_runner.py --project reid --summary
```
