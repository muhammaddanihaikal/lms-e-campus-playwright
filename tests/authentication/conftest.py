"""Fixture spesifik module authentication."""

import json
from pathlib import Path

import pytest

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "authentication"


@pytest.fixture
def valid_login_data():
    with open(DATA_DIR / "valid_login.json") as f:
        return json.load(f)


@pytest.fixture
def invalid_login_data():
    with open(DATA_DIR / "invalid_login.json") as f:
        return json.load(f)
