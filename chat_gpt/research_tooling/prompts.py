import textwrap
from pathlib import Path

STEP1_METHOD = """\
## Passo 1: Primeira passada
A primeira passada é uma rápida análise para obter uma visão geral do artigo. Você também pode decidir se precisa fazer mais passadas. Essa passada deve gerar uma leitura de cerca de cinco a dez minutos e consiste nos seguintes passos:
1. Ler cuidadosamente o título, abstract e introdução
2. Ler os títulos das seções e subseções, mas ignorar tudo o resto
3. Ler as conclusões
4. Dar uma olhada rápida nas referências, escrevendo mentalmente os nomes dos que já leu

No final da primeira passada, você deve ser capaz de responder aos cinco P's:
1. Categoria: Qual tipo de artigo é esse? Um artigo de medição? Uma análise de um sistema existente? Uma descrição de um protótipo de pesquisa?
2. Contexto: Quais outros artigos são relacionados a esse? Quais bases teóricas foram usadas para analisar o problema?
3. Corretude: As suposições parecem válidas?
4. Contribuições: Quais são as principais contribuições do artigo?
5. Clareza: O artigo está bem escrito?
"""

STEP2_METHOD = """\
## Passo 2: Segunda passada
Na segunda passada, leia o artigo com mais atenção, mas ignore detalhes como provas. Ajuda a escrever os pontos-chave ou a fazer comentários nas margens enquanto você lê.
1. Olhe cuidadosamente nas figuras, diagramas e outras ilustrações no artigo. Dê atenção especial aos gráficos.
   São as espinhas dos dedos? São as legendas corretas? São os resultados apresentados com erros de medida, de forma que as conclusões sejam estatisticamente significativas? Erros comuns como esses separam trabalho rápido e mal feito do verdadeiramente excelente.
2. Lembre-se de marcar as referências relevantes para leitura posterior (essas são ótimas para aprender mais sobre o contexto do artigo).

A segunda passada deve levar até uma hora. No final dessa passada, você deve ser capaz de compreender o conteúdo do artigo. Você deve ser capaz de resumir a principal proposta do artigo, com evidências suportadas, para alguém. Esse é o nível de detalhe apropriado para artigos nos quais você está interessado, mas não está na sua área de especialidade.

Às vezes, até o final da segunda passada, você não entenderá o artigo. Isso pode ser porque o assunto é novo para você, com termos e acrônimos desconhecidos. Ou os autores podem usar uma prova ou uma técnica experimental que você não entende, de sorte, o conteúdo principal do artigo é incompreensível. O artigo pode ser mal escrito com afirmações não substanciadas e muitas referências futuras. Ou pode ser que seja tarde de noite e você está cansado.

Você pode agora escolher deixar o artigo de lado, retornar ao artigo posteriormente, ou persistir e prosseguir para a terceira passada.
"""

STEP3_METHOD = """\
## Passo 3: Terceira passada
Para compreender completamente um artigo, especialmente se você é um revisor, é necessário fazer uma terceira passada. A chave para a terceira passada é tentar recriá-lo virtualmente: ou seja, fazer as mesmas suposições dos autores, recriar o trabalho. Comparando isso com o artigo real, você pode facilmente identificar as inovações do artigo e seus pontos fracos.

Essa passada requer muita atenção aos detalhes. Você deve identificar e desafiar todas as suposições em cada declaração. Além disso, você deve pensar sobre como apresentaria um determinado conceito.

Essa comparação entre o real e virtual lhe dará um insight muito mais profundo sobre as técnicas de prova e apresentação no artigo e pode facilmente adicionar isso à sua coleção de ferramentas. Durante essa passada, você também deve anotar ideias para futuros trabalhos.

A terceira passada pode levar cerca de quatro ou cinco horas para iniciantes e cerca de uma hora para um leitor experiente. No final dessa passada, você deve ser capaz de reconstruir a estrutura todo do artigo de memória, bem como ser capaz de identificar seus pontos fortes e fracos. Em particular, você deve ser capaz de identificar suposições implícitas, referências ausentes para trabalho relevante e possíveis problemas com técnicas experimentais ou analíticas.
"""


def make_prompt(
    *,
    system_text: str,
    objective: str,
    paper_slug: str,
    step_number: int,
    max_step: int,
    criticality: str,
    output_root: Path,
    paper_content: str = "",
    focus_content: str = "",
) -> str:
    step_name = {
        1: "Primeira passada",
        2: "Segunda passada",
        3: "Terceira passada",
        4: "Extração de Referências",
        5: "Ideias e Trabalhos Futuros",
    }[step_number]
    
    # Truncate content if too huge? GPT-4o typically handles it.
    # Let's verify if paper_content is empty
    content_block = ""
    if paper_content:
        content_block = f"TEXTO DO PAPER:\n{paper_content}"
    else:
        content_block = f"TEXTO DO PAPER EM: {output_root / paper_slug / 'paper_text.md'} (Por favor, leia este arquivo)"

    focus_block = ""
    if focus_content:
        focus_block = textwrap.dedent(f"""
            # FOCO DO PROJETO (PRIORIDADE MÁXIMA)
            O usuário definiu o seguinte foco para este projeto. A análise deve sempre conectar o paper a este tema:
            "{focus_content}"
            
            IMPORTANTE: Adicione uma seção final '## Análise de Foco' explicando detalhadamente como este paper aborda ou contribui para o foco acima.
        """)

    instructions = []
    
    # Global Rules for all steps
    instructions.append("**REGRAS ESTRITAS DE FORMATAÇÃO (PARA TODAS AS ETAPAS)**:")
    instructions.append("1. NÃO inclua textos introdutórios (ex: 'Você está executando...', 'Seguem os resultados...').")
    instructions.append("2. NÃO repita seções como '# Objetivo', '# Metadados', '# Referência do paper'.")
    instructions.append("3. Comece a resposta DIRETAMENTE com o conteúdo solicitado no template.")
    
    if step_number == 1:
        instructions.append("REGRAS ESPECÍFICAS DO PASSO 1:")
        instructions.append("- PRIMEIRA SEÇÃO (NO TOPO): Crie '## Resumo Geral' com um parágrafo conciso sobre o que é o trabalho.")
        instructions.append("- LOGO APÓS O RESUMO: Crie '## Problema' e descreva em UMA ÚNICA FRASE qual o problema/lacuna que o paper resolve.")
        instructions.append("- Na seção 'Leitura rápida': Liste APENAS títulos de seções (sem figuras/tabelas).")
        instructions.append("- NÃO inclua 'Avaliação sucinta' ou 'Recomendação'.")
        instructions.append("- OBRIGATÓRIO: Adicione '## Abstract Traduzido' e '## Conclusão Traduzida' e '## Análise de Foco' no final.")
        
    if step_number == 2:
        instructions.append("REGRAS ESPECÍFICAS DO PASSO 2:")
        instructions.append("- Nos 'Pontos-chave': NÃO use citações de página/seção.")
        instructions.append("- REMOVA TOTALMENTE a seção de 'Análise das figuras/tabelas'.")
        instructions.append("- OBRIGATÓRIO: Adicione '## Análise de Foco' no final.")
        
    if step_number == 4:
        instructions.append("REGRAS ESPECÍFICAS DO PASSO 4 (REFERÊNCIAS):")
        instructions.append("- Liste as 5 referências mais importantes mencionadas no texto.")
        instructions.append("- Para cada uma, explique BREVEMENTE por que é importante no contexto do paper.")
        instructions.append("- Formato sugerido: '- [X] Autor et al. (Ano) - Título: Explicação...'")
        instructions.append("- NÃO inclua 'Análise de Foco' neste passo.")
        
    if step_number == 5:
        instructions.append("REGRAS ESPECÍFICAS DO PASSO 5 (TRABALHOS FUTUROS):")
        instructions.append("- Liste TODAS as ideias de trabalhos futuros propostas pelos autores.")
        instructions.append("- Adicione uma seção '## Minhas Sugestões (Criativas)': Proponha 2 novas ideias baseadas no potencial do trabalho.")
        instructions.append("- Seja criativo e visionário nestas 2 sugestões.")
        instructions.append("- NÃO inclua 'Análise de Foco' neste passo.")

    formatted_instructions = "\n".join(instructions)
    
    method_text = ""
    if step_number == 1:
        method_text = STEP1_METHOD.strip()
    elif step_number == 2:
        method_text = STEP2_METHOD.strip()
    elif step_number == 3:
        method_text = STEP3_METHOD.strip()
    elif step_number == 4:
        method_text = "PASSO EXTRA: Extração de Referências Prioritárias.\nAnalise a seção de Referências e as citações no texto para identificar as 5 obras fundamentais para entender este trabalho."
    elif step_number == 5:
        method_text = "PASSO EXTRA: Ideias e Trabalhos Futuros.\nIdentifique o que os autores disseram que fariam a seguir, e então use sua criatividade para propor novos caminhos de pesquisa."

    return textwrap.dedent(
        f"""\
        {system_text.strip()}

        <USER>
        # Objetivo
        {objective}
        
        {focus_block if step_number not in (4, 5) else ""}

        # Paper (entrada)
        {content_block}

        # Instruções de Metadados
        NÃO gere metadados no corpo da resposta.

        # Etapa atual
        Você está executando o **Passo {step_number}: {step_name}**.

        {formatted_instructions}

        {method_text}
        </USER>
        """
    )




def make_metadata_prompt(paper_content: str) -> str:
    return textwrap.dedent(f"""\
        Você é um assistente bibliográfico preciso.
        
        TAREFA: Analise o texto do paper fornecido abaixo e extraia os metadados bibliográficos.
        
        TEXTO DO PAPER:
        {paper_content[:50000]}  # Limitando para evitar estouro de contexto se for gigante, mas 50k chars deve dar.

        FORMATO DE SAÍDA (Estrito):
        Retorne APENAS as linhas abaixo, preenchendo o que encontrar. Se não encontrar, deixe em branco.
        Título: <Título exato>
        Autores: <Lista de autores separados por ponto e vírgula>
        Ano: <Ano de publicação>
        Venue: <Conferência ou Journal>
        DOI/URL: <DOI ou Link se houver>
        Tags: <3-5 tags curtas sobre a área (ex: Computer Vision, Re-ID)>
        Keywords: <Palavras-chave listadas no paper>
        
        Não adicione marcação markdown extra além das chaves.
    """)
