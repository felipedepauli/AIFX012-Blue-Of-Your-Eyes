import pytest
from pathlib import Path
import sys

# Ensure chat_gpt is in path for tests
repo_root = Path(__file__).resolve().parent.parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

@pytest.fixture
def repo_root_path():
    return repo_root

@pytest.fixture
def dummy_pdf_path(tmp_path):
    # Retrieve a dummy PDF path that exists
    p = tmp_path / "dummy.pdf"
    p.write_bytes(b"%PDF-1.4 header dummy content")
    return p
