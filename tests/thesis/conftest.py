"""Fixture spesifik module thesis (E2E full flow)."""

import pytest

from pages.kaprodi.defense_documents_page import KaprodiDefenseDocumentsPage
from pages.kaprodi.thesis_approval_page import KaprodiApprovalPage
from pages.lecturer.thesis_progress_page import LecturerThesisProgressPage
from pages.login_page import LoginPage
from pages.navbar_page import NavBarPage
from pages.student.thesis_page import StudentThesisPage


@pytest.fixture
def thesis_actors(page):
    """Bundle helper page-objects + login utility untuk e2e flow."""
    return {
        "login": LoginPage(page),
        "navbar": NavBarPage(page),
        "student_thesis": StudentThesisPage(page),
        "kaprodi_approval": KaprodiApprovalPage(page),
        "kaprodi_defense": KaprodiDefenseDocumentsPage(page),
        "lecturer_progress": LecturerThesisProgressPage(page),
    }
