"""Fixture spesifik module lecturer."""

import pytest

from pages.lecturer.thesis_progress_page import LecturerThesisProgressPage


@pytest.fixture
def lecturer_progress_page(logged_in_as_lecturer):
    return LecturerThesisProgressPage(logged_in_as_lecturer)
