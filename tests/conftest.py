"""Level 2 conftest — fixture login per role + page object umum.

Hierarki fixture:
  - logged_in_as_admin_office  → login sebagai admin office, balik raw page
  - logged_in_as_kaprodi       → login sebagai kaprodi
  - logged_in_as_lecturer      → login sebagai lecturer (dosen)
  - logged_in_as_student       → login sebagai mahasiswa
"""

import json
from pathlib import Path

import pytest

from pages.login_page import LoginPage

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _load_login_credentials():
    with open(DATA_DIR / "authentication" / "valid_login.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def login_credentials():
    return _load_login_credentials()


def _login_as(page, credential, expected_url):
    login = LoginPage(page)
    login.open()
    login.login(credential, expected_url=expected_url)
    return page


@pytest.fixture(scope="function")
def logged_in_as_admin_office(page, login_credentials):
    return _login_as(page, login_credentials["admin_office"], expected_url="**/Adminoffice**")


@pytest.fixture(scope="function")
def logged_in_as_kaprodi(page, login_credentials):
    return _login_as(page, login_credentials["kaprodi"], expected_url="**/Adminkaprodi*")


@pytest.fixture(scope="function")
def logged_in_as_lecturer(page, login_credentials):
    return _login_as(page, login_credentials["lecturer"], expected_url="**/E-Campus/**")


@pytest.fixture(scope="function")
def logged_in_as_student(page, login_credentials):
    return _login_as(page, login_credentials["student"], expected_url="**/home*")
