"""Fixture spesifik module student."""

import json
from pathlib import Path

import pytest

from pages.student.thesis_page import StudentThesisPage

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "thesis"


@pytest.fixture
def valid_proposal_data():
    with open(DATA_DIR / "valid_proposal.json") as f:
        return json.load(f)


@pytest.fixture
def student_thesis_page(logged_in_as_student):
    page = logged_in_as_student
    return StudentThesisPage(page)
