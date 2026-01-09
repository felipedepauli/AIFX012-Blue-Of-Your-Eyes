import argparse
import sys
from pathlib import Path
from typing import Iterable, Optional

from .paths import PaperPaths, build_paths, ensure_dir, write_if_missing, read_text_file, slugify
from .status import read_status, set_status, next_step_from_status, STATUS_ORDER
from .pdf_extract import extract_pdf_text
from .templates import make_metadata_template, make_pass_template, make_readme_template, make_triage_template
from .prompts import make_prompt
from .summary import generate_summary
from .llm_client import query_llm


LOW_MODEL = "gpt-5-nano"
HIGH_MODEL = "gpt-5-mini"

def prepare_paper(
    *,
    pdf_path: Path,
    output_root: Path,
    slug: str,
    objective: str,
    max_step: int,
    criticality: str,
    methodology_path: Path,
    focus_content: str = "",
) -> PaperPaths:
    paths = build_paths(output_root=output_root, slug=slug)
    ensure_dir(paths.out_dir)

    title_guess = pdf_path.stem.replace("_", " ")

    created_any = False
    created_any |= write_if_missing(paths.metadata, make_metadata_template(pdf_path=pdf_path, title_guess=title_guess))
    created_any |= write_if_missing(paths.triage_report, make_triage_template(title_guess=title_guess))
    created_any |= write_if_missing(paths.first_pass, make_pass_template("Passo 1: Primeira passada"))
    created_any |= write_if_missing(paths.second_pass, make_pass_template("Passo 2: Segunda passada"))
    created_any |= write_if_missing(paths.third_pass, make_pass_template("Passo 3: Terceira passada"))
    created_any |= write_if_missing(paths.references, make_pass_template("Referências para ler"))
    created_any |= write_if_missing(paths.ideas, make_pass_template("Ideias / trabalhos futuros"))
    created_any |= write_if_missing(paths.readme, make_readme_template(slug))

    if not paths.extracted_text.exists():
        extracted = extract_pdf_text(pdf_path)
        paths.extracted_text.write_text(extracted, encoding="utf-8")
        created_any = True

    paper_text_content = read_text_file(paths.extracted_text) or ""

    system_text = read_text_file(methodology_path)
    if not system_text:
        raise RuntimeError(f"Não encontrei o arquivo de system prompt em: {methodology_path}")

    paths.prompt_step1.write_text(
        make_prompt(
            system_text=system_text,
            objective=objective,
            paper_slug=slug,
            step_number=1,
            max_step=max_step,
            criticality=criticality,
            output_root=output_root,
            paper_content=paper_text_content,
            focus_content=focus_content,
        ),
        encoding="utf-8",
    )
    paths.prompt_step2.write_text(
        make_prompt(
            system_text=system_text,
            objective=objective,
            paper_slug=slug,
            step_number=2,
            max_step=max_step,
            criticality=criticality,
            output_root=output_root,
            paper_content=paper_text_content,
            focus_content=focus_content,
        ),
        encoding="utf-8",
    )
    paths.prompt_step3.write_text(
        make_prompt(
            system_text=system_text,
            objective=objective,
            paper_slug=slug,
            step_number=3,
            max_step=max_step,
            criticality=criticality,
            output_root=output_root,
            paper_content=paper_text_content,
            focus_content=focus_content,
        ),
        encoding="utf-8",
    )
    paths.prompt_step4.write_text(
        make_prompt(
            system_text=system_text,
            objective=objective,
            paper_slug=slug,
            step_number=4,
            max_step=max_step,
            criticality=criticality,
            output_root=output_root,
            paper_content=paper_text_content,
            # focus_content sent (although prompt ignores it for step 4 as per prompt logic, or we can omit)
            focus_content=focus_content,
        ),
        encoding="utf-8",
    )
    paths.prompt_step5.write_text(
        make_prompt(
            system_text=system_text,
            objective=objective,
            paper_slug=slug,
            step_number=5,
            max_step=max_step,
            criticality=criticality,
            output_root=output_root,
            paper_content=paper_text_content,
            focus_content=focus_content,
        ),
        encoding="utf-8",
    )

    if created_any:
        print(f"[ok] Preparado: {paths.out_dir}")
    else:
        print(f"[ok] Já existia (sem mudanças): {paths.out_dir}")

    return paths


def iter_pdfs(docs_dir: Path) -> Iterable[Path]:
    for p in sorted(docs_dir.glob("*.pdf")):
        if p.is_file():
            yield p


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Prepara estrutura e prompts para análise de PDFs em research/docs, escrevendo em research/pdf/<slug>/.",
    )
    parser.add_argument("--pdf", action="append", help="Caminho do PDF (pode repetir). Se omitido, usa --all.")
    parser.add_argument("--all", action="store_true", help="Processa todos os PDFs em research/docs")
    parser.add_argument("--project", help="Nome do projeto (ex: reid). Define caminhos padrão em projects/<project>.")
    parser.add_argument("--docs-dir", help="Diretório de PDFs de entrada (padrão: research/docs ou projects/<project>/docs)")
    parser.add_argument("--output-root", help="Diretório base para saídas (padrão: research/pdf ou projects/<project>/pdf)")
    parser.add_argument("--slug", help="Força o PAPER_SLUG (válido apenas quando há um único --pdf)")
    parser.add_argument("--objective", default="(preencha aqui)", help="Objetivo da análise")
    parser.add_argument("--max-step", type=int, default=3, choices=[1, 2, 3, 4, 5], help="Profundidade máxima (5 = inclui future work)")
    parser.add_argument("--criticality", default="médio", choices=["baixo", "médio", "alto"], help="Nível de criticidade")
    parser.add_argument(
        "--no-interactive",
        action="store_true",
        help="Não pausar entre PDFs (processa todos sem perguntar)",
    )
    parser.add_argument(
        "--interactive-steps",
        action="store_true",
        help="Executa modo interativo por ETAPA (Passo 1/2/3): mostra o prompt e pergunta se avança",
    )
    parser.add_argument(
        "--print-prompt",
        action="store_true",
        help="Imprime o texto do prompt (para copiar/colar) em vez de só mostrar o caminho do arquivo",
    )
    parser.add_argument(
        "--no-update-status",
        action="store_true",
        help="Não atualiza automaticamente o Status no 00_metadata.md quando você confirma avanço de etapa",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Gera o arquivo candidates_summary.md agregando todos os papers processados.",
    )
    parser.add_argument(
        "--auto-run",
        action="store_true",
        help="Executa automaticamente a etapa atual usando o LLM (requer chave OpenAI no .env).",
    )
    parser.add_argument(
        "--model",
        default=HIGH_MODEL,
        help=f"Modelo OpenAI para usar no --auto-run (padrão: {HIGH_MODEL}).",
    )
    parser.add_argument(
        "--extract-metadata",
        action="store_true",
        help=f"Extrai metadados (Autores, Venue, etc) usando {LOW_MODEL} automaticamente.",
    )

    args = parser.parse_args(argv)

    repo_root = Path.cwd()

    if args.project:
        project_dir = repo_root / "projects" / args.project
        if not project_dir.exists():
             # Criar warning ou erro? Melhor só usar path resolution, se não existir o docs estoura erro depois.
            pass
        
        docs_dir = project_dir / "docs"
        if args.docs_dir:
            docs_dir = repo_root / args.docs_dir
            
        output_root = project_dir / "pdf"
        if args.output_root:
            output_root = repo_root / args.output_root
            
        summary_root = project_dir # Summary goes to project root
        
        # Check for focus.md
        focus_path = project_dir / "focus.md"
        focus_content = read_text_file(focus_path) or ""
        if focus_content:
             print(f"-> Foco do projeto detectado em: {focus_path}")
    else:
        docs_dir = repo_root / (args.docs_dir or "research/docs")
        output_root = repo_root / (args.output_root or "research/pdf")
        summary_root = repo_root
        focus_content = ""
    
    # Handle Summary generation
    if args.summary:
        generate_summary(output_root=output_root, project_root=summary_root)
        return 0

    # Try to find methodology.md in known locations
    # 1. research/methodology.md (relative to repo_root)
    # 2. chat_gpt/scripts/methodology.md (legacy)
    
    candidates = [
        repo_root / "chat_gpt" / "system" / "methodology.md",
        repo_root / "research" / "methodology.md",
        repo_root / "chat_gpt" / "scripts" / "methodology.md",
    ]
    methodology_path = None
    for c in candidates:
        if c.exists():
            methodology_path = c
            break
            
    if not methodology_path:
        # Fallback to error or default
        methodology_path = repo_root / "chat_gpt" / "system" / "methodology.md"

    if args.all:
        pdfs = list(iter_pdfs(docs_dir))
    else:
        pdfs = [Path(p) for p in (args.pdf or [])]

    if not pdfs:
        parser.error("Informe --pdf <arquivo.pdf> (pode repetir) ou use --all")

    if args.slug and len(pdfs) != 1:
        parser.error("--slug só pode ser usado quando há exatamente um --pdf")

    for pdf_path in pdfs:
        if not pdf_path.is_absolute():
            pdf_path = repo_root / pdf_path
        if not pdf_path.exists():
            print(f"Aviso: PDF não encontrado ignorado: {pdf_path}")
            continue

        slug = args.slug or slugify(pdf_path.stem)

        paths = prepare_paper(
            pdf_path=pdf_path,
            output_root=output_root,
            slug=slug,
            objective=args.objective,
            max_step=args.max_step,
            criticality=args.criticality,
            methodology_path=methodology_path,
            focus_content=focus_content,
        )
    
        if args.extract_metadata:
            from .prompts import make_metadata_prompt
            import re
            
            print(f"--- Extraindo Metadados ({LOW_MODEL}) ---")
            extracted_text = read_text_file(paths.extracted_text)
            
            if extracted_text:
                meta_prompt = make_metadata_prompt(extracted_text)
                try:
                    resp_meta = query_llm(meta_prompt, model=LOW_MODEL)
                    if resp_meta:
                        current_meta = read_text_file(paths.metadata) or ""
                        new_data = {}
                        for line in resp_meta.splitlines():
                            if ":" in line:
                                k, v = line.split(":", 1)
                                new_data[k.strip().lower()] = v.strip()
                        
                        lines = current_meta.splitlines()
                        out_lines = []
                        update_count = 0
                        for line in lines:
                            m = re.match(r"^-\s*([^:]+):(.*)$", line)
                            if m:
                                key = m.group(1).strip()
                                key_lower = key.lower()
                                if key_lower in new_data and new_data[key_lower]:
                                    line = f"- {key}: {new_data[key_lower]}"
                                    update_count += 1
                            out_lines.append(line)
                        
                        paths.metadata.write_text("\n".join(out_lines), encoding="utf-8")
                        print(f"[ok] Metadados atualizados ({update_count} campos) em {paths.metadata}")
                    else:
                         print("[Erro] Resposta vazia do LLM para metadados.")
                except Exception as e:
                    print(f"[Erro] Falha na extração de metadados: {e}")

        status = read_status(paths.metadata)
        
        # Determine next step
        # Logic: 
        # - If Triage is empty/not filled, suggest Triage? 
        # - Current logic `next_step_from_status` maps statuses to steps 1, 2, 3.
        # - Triage is step 0 basically. "triagem" status means -> Ready for Step 1? Or doing Triage?
        # - "triagem" in status.py maps to 1. This means extraction is done, metadata is done, ready for First Pass.
        # - Wait, where is the Triage execution step?
        #   PRD says: Ingestion -> Triage -> Layered Reading.
        #   If status is 'triagem', it means it IS IN triage stage? Or completed triage?
        #   Ah, status.py says: "triagem" -> next step 1.
        #   This implies "triagem" status designates the START state.
        #   So Step 1 is "First Pass".
        #   We need to handle the "Triage report generation" logic.
        #   The prompt for Triage is... where? 
        #   `templates.py` has `triage_report.md` template. 
        #   We need a prompt to FILL `triage_report.md`.
        #   Currently we don't have a `prompt_triage.md`.
        #   Let's check `prompts.py` (I can't check now effectively without opening it, but I recall creating prompt_step1/2/3).
        #   If User wants auto-run for Triage, we need a Triage Prompt. 
        #   For now, we'll focus on Steps 1, 2, 3 which have prompts.
        
        step = next_step_from_status(status, args.max_step)

        def prompt_path_for(step_number: int) -> Path:
            if step_number == 1:
                return paths.prompt_step1
            if step_number == 2:
                return paths.prompt_step2
            if step_number == 3:
                return paths.prompt_step3
            if step_number == 4:
                return paths.prompt_step4
            if step_number == 5:
                return paths.prompt_step5
            raise ValueError(f"Passo inválido: {step_number}")
            
        def output_path_for(step_number: int) -> Path:
            if step_number == 1:
                return paths.first_pass
            if step_number == 2:
                return paths.second_pass
            if step_number == 3:
                return paths.third_pass
            if step_number == 4:
                return paths.references
            if step_number == 5:
                # Use paths.ideas (05_ideas_future_work.md)
                return paths.ideas
            raise ValueError(f"Passo inválido: {step_number}")

        def status_after_step(step_number: int) -> str:
            return {
                1: "lido-1a-passada",
                2: "lido-2a-passada",
                3: "lido-3a-passada",
                4: "extraindo-referencias",
                5: "extraindo-ideias",
            }[step_number]

        if step is None:
            print(f"\n[ok] '{slug}': Completo ou sem próximos passos (Status: {status})")
        else:
            print(f"\nProcessando '{slug}' (Status: {status} -> Passo {step})")

        # AUTO RUN LOOP
        if (args.interactive_steps or args.auto_run) and step is not None:
            while step is not None:
                ppath = prompt_path_for(step)
                
                if args.auto_run:
                    # Select model
                    current_model = args.model
                    if step == 4:
                        current_model = LOW_MODEL

                    print(f"--- Auto-Run: Executando Passo {step} ({current_model}) ---")
                    prompt_text = read_text_file(ppath)
                    if not prompt_text:
                        print(f"Erro: Prompt vazio em {ppath}")
                        break
                        
                    print(f"Enviando para LLM... (pode demorar)")
                    response = query_llm(prompt_text, model=current_model)
                    
                    if response:
                        out_file = output_path_for(step)
                        # Append or Overwrite? Usually overwrite the template or append to it?
                        # The template has a header. The LLM output usually is the content.
                        # Let's simple write.
                        out_file.write_text(response, encoding="utf-8")
                        print(f"Resultado salvo em: {out_file}")
                        
                        if not args.no_update_status:
                            new_st = status_after_step(step)
                            set_status(paths.metadata, new_st)
                            print(f"Status atualizado para: {new_st}")
                    else:
                         print("Falha na chamada do LLM (resposta vazia).")
                         break
                else:
                    # Manual interactive interface
                    print("\n====================")
                    print(f"PROMPT (Passo {step}) -> {ppath}")
                    print("====================\n")
                    if args.print_prompt:
                        prompt_text = read_text_file(ppath) or ""
                        sys.stdout.write(prompt_text)
                        if not prompt_text.endswith("\n"):
                            sys.stdout.write("\n")
                    else:
                        print(f"Cole o conteúdo de `{ppath}` no Windsurf.")

                    resp = input("\nApós concluir esse passo no Windsurf, avançar para o próximo? (s/N): ").strip().lower()
                    if resp not in {"s", "sim", "y", "yes"}:
                        break
                    
                    if not args.no_update_status:
                        set_status(paths.metadata, status_after_step(step))

                status = read_status(paths.metadata)
                step = next_step_from_status(status, args.max_step)

            print(f"\n[ok] Fim do processamento para {slug}.")
        else:
            # Just preparation report
            if step is not None:
                print("\nPróximo passo no Windsurf:")
                print(f"- Passo 1: cole o conteúdo de `{paths.prompt_step1}` no chat/comando")
                if args.max_step >= 2:
                    print(f"- Passo 2: cole `{paths.prompt_step2}` depois de concluir o passo 1")
                if args.max_step >= 3:
                    print(f"- Passo 3: cole `{paths.prompt_step3}` depois de concluir o passo 2")

        if not args.no_interactive and not args.auto_run:
            if len(pdfs) > 1:
                resp = input("\nContinuar para o próximo PDF? (s/N): ").strip().lower()
                if resp not in {"s", "sim", "y", "yes"}:
                    break

    return 0
