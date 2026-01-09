#!/usr/bin/env python3

import sys
from pathlib import Path

# Adiciona o diretório raiz ao PYTHONPATH para permitir imports de chat_gpt.research_tooling
# Supondo que este script está em chat_gpt/scripts/
# repo_root é ../../
repo_root = Path(__file__).resolve().parent.parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from chat_gpt.research_tooling.cli import main

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
