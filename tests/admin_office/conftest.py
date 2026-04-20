"""Fixture spesifik module admin_office.

Menyediakan:
  - master_student_page, master_kaprodi_page, master_lecturer_page, master_course_page
  - admission_page, approval_page (admission tidak butuh login)
"""

import pytest

from pages.admin_office.admission.admission_page import AdmissionPage, ApprovalPage
from pages.admin_office.master.master_course.master_course_page import MasterCoursePage
from pages.admin_office.master.master_kaprodi.master_kaprodi_page import MasterKaprodiPage
from pages.admin_office.master.master_lecturer.master_lecturer_page import MasterLecturerPage
from pages.admin_office.master.master_student.master_student_page import MasterStudentPage


@pytest.fixture
def master_student_page(logged_in_as_admin_office):
    page = logged_in_as_admin_office
    pg = MasterStudentPage(page)
    pg.navigate()
    return pg


@pytest.fixture
def master_kaprodi_page(logged_in_as_admin_office):
    page = logged_in_as_admin_office
    pg = MasterKaprodiPage(page)
    pg.navigate()
    return pg


@pytest.fixture
def master_lecturer_page(logged_in_as_admin_office):
    page = logged_in_as_admin_office
    pg = MasterLecturerPage(page)
    pg.navigate()
    return pg


@pytest.fixture
def master_course_page(logged_in_as_admin_office):
    page = logged_in_as_admin_office
    pg = MasterCoursePage(page)
    pg.navigate()
    return pg


@pytest.fixture
def admission_page(page):
    pg = AdmissionPage(page)
    pg.navigate()
    return pg


@pytest.fixture
def approval_page(logged_in_as_admin_office):
    page = logged_in_as_admin_office
    pg = ApprovalPage(page)
    pg.navigate()
    return pg
