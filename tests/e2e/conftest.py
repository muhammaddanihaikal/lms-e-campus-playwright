"""Fixture spesifik module e2e — full user journey tests."""

import pytest

from pages.admin_office.admission.admission_page import AdmissionPage, ApprovalPage
from pages.admin_office.master.master_student.master_student_page import MasterStudentPage
from pages.kaprodi.defense_documents_page import KaprodiDefenseDocumentsPage
from pages.kaprodi.thesis_approval_page import KaprodiApprovalPage
from pages.lecturer.thesis_progress_page import LecturerThesisProgressPage
from pages.login_page import LoginPage
from pages.navbar_page import NavBarPage
from pages.student.thesis_page import StudentThesisPage


@pytest.fixture
def student_e2e_actors(page):
    """Bundle for student E2E flow."""
    return {
        "login": LoginPage(page),
        "navbar": NavBarPage(page),
        "thesis": StudentThesisPage(page),
    }


@pytest.fixture
def kaprodi_e2e_actors(page):
    """Bundle for kaprodi E2E flow."""
    return {
        "login": LoginPage(page),
        "navbar": NavBarPage(page),
        "approval": KaprodiApprovalPage(page),
        "defense": KaprodiDefenseDocumentsPage(page),
    }


@pytest.fixture
def lecturer_e2e_actors(page):
    """Bundle for lecturer E2E flow."""
    return {
        "login": LoginPage(page),
        "navbar": NavBarPage(page),
        "progress": LecturerThesisProgressPage(page),
    }


@pytest.fixture
def admin_office_e2e_actors(page):
    """Bundle for admin office E2E flow."""
    return {
        "login": LoginPage(page),
        "navbar": NavBarPage(page),
        "admission": AdmissionPage(page),
        "approval": ApprovalPage(page),
        "student": MasterStudentPage(page),
    }
