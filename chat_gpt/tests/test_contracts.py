import pytest
from chat_gpt.research_tooling.status import STATUS_TO_NEXT_STEP, STATUS_ORDER, parse_status

def test_status_contract_compliance():
    """
    Validates that status.py implements the statuses defined in 04_DATA_CONTRACTS.md.
    Contract:
    Status válidos: triagem | lido-1a-passada | lido-2a-passada | lido-3a-passada | arquivado | candidato
    """
    expected_statuses = {
        "triagem",
        "lido-1a-passada",
        "lido-2a-passada",
        "lido-3a-passada",
        # Terminal states / outcomes
        "arquivado",
        "candidato",
    }
    
    implemented_statuses = set(STATUS_TO_NEXT_STEP.keys())
    assert expected_statuses.issubset(implemented_statuses), \
        f"Missing statuses in implementation: {expected_statuses - implemented_statuses}"
    
    assert set(STATUS_ORDER) == implemented_statuses, "STATUS_ORDER should match keys of STATUS_TO_NEXT_STEP"

def test_parse_status_robustness():
    """Ensures parse_status handles whitespace and case correctly (if desired) or strictness"""
    assert parse_status("- Status: triagem") == "triagem"
    assert parse_status("- Status:   lido-1a-passada   ") == "lido-1a-passada"
    # Test strictness: if it's not a valid status, it defaults to triagem per current implementation
    assert parse_status("- Status: invalid") == "triagem"

def test_terminal_states():
    """Arquivado and Candidato should not suggest a next step in the reading pipeline"""
    assert STATUS_TO_NEXT_STEP["arquivado"] is None
    assert STATUS_TO_NEXT_STEP["candidato"] is None
