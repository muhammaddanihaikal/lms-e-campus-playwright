"""Fixture spesifik module kaprodi."""

import json
from pathlib import Path

import pytest

from pages.kaprodi.thesis_approval_page import KaprodiApprovalPage
from pages.kaprodi.defense_documents_page import KaprodiDefenseDocumentsPage

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


@pytest.fixture
def valid_approval_data():
    with open(DATA_DIR / "thesis" / "valid_approval.json") as f:
        return json.load(f)


@pytest.fixture
def kaprodi_approval_page(logged_in_as_kaprodi):
    return KaprodiApprovalPage(logged_in_as_kaprodi)


@pytest.fixture
def kaprodi_defense_page(logged_in_as_kaprodi):
    return KaprodiDefenseDocumentsPage(logged_in_as_kaprodi)
