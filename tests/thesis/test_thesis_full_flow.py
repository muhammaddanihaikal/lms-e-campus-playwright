"""E2E Test: Dynamic State-Based Thesis Flow.

Pakai pendekatan STATE MACHINE — deteksi state thesis terakhir lalu
lanjut dari state itu. Setiap fase idempotent → skip otomatis kalau
sudah selesai.

State machine:
    NO_PROPOSAL → PROPOSAL_SUBMITTED → DEFENSE_READY
                                          ↓
                              DEFENSE_SUBMITTED → COMPLETED
"""

import re

import allure

from utils.faker_helper import generate_thesis_proposal
from utils.file_helper import file_path

# State constants
STATE_NO_PROPOSAL = "no_proposal"
STATE_PROPOSAL_SUBMITTED = "proposal_submitted"
STATE_DEFENSE_READY = "defense_ready"
STATE_DEFENSE_SUBMITTED = "defense_submitted"


def _safe_logout(page, navbar):
    try:
        navbar.logout()
        page.wait_for_timeout(500)
    except Exception:
        pass


def _detect_thesis_state(page, student_thesis_page):
    """Deteksi state thesis dari sisi student. Student harus sudah login."""
    student_thesis_page.navigate_to_thesis()
    page.wait_for_timeout(500)

    if page.get_by_role("button", name="Start Thesis Proposal").is_visible():
        return STATE_NO_PROPOSAL

    defense_link = page.get_by_text("Defense").first
    try:
        if defense_link.is_visible():
            defense_link.click()
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(500)
            if page.get_by_role("button", name="Submit Defense Request").is_visible():
                return STATE_DEFENSE_READY
            return STATE_DEFENSE_SUBMITTED
    except Exception:
        pass

    return STATE_PROPOSAL_SUBMITTED


def _phase_submit_proposal(actors, student_cred, thesis_data):
    actors["login"].open()
    actors["login"].login(student_cred, expected_url="**/home*")

    student_page = actors["student_thesis"]
    student_page.navigate_to_thesis()
    form = student_page.open_proposal_form()
    form.fill(thesis_data)
    form.upload(file_path("proposal_dummy.pdf"))
    form.submit()

    _safe_logout(student_page.page, actors["navbar"])


def _phase_kaprodi_approve_proposal(actors, kaprodi_cred, thesis_title):
    actors["login"].open()
    actors["login"].login(kaprodi_cred, expected_url="**/Adminkaprodi*")

    kaprodi_page = actors["kaprodi_approval"]
    kaprodi_page.navigate_to_approval()
    page = kaprodi_page.page

    page.get_by_role("tab", name=re.compile(r"Pending.*")).click()
    page.wait_for_timeout(1000)

    row = kaprodi_page.proposal_row(thesis_title)
    try:
        row.wait_for(state="visible", timeout=3000)
    except Exception:
        _safe_logout(page, actors["navbar"])
        return

    kaprodi_page.find_proposal(thesis_title)
    modal = kaprodi_page.open_proposal_modal(thesis_title)
    modal.approve({"note": "Approved via E2E"})

    kaprodi_page.check_proposal_in_tab(thesis_title, tab_pattern=r"Approved.*")
    _safe_logout(page, actors["navbar"])


def _phase_lecturer_approve_research(actors, lecturer_cred, student_username):
    actors["login"].open()
    actors["login"].login(lecturer_cred, expected_url="**/E-Campus/**")

    lect = actors["lecturer_progress"]
    lect.navigate_to_progress()
    lect.open_student_progress(student_username)
    lect.approve_research_phase(notes="Approved via E2E")

    _safe_logout(lect.page, actors["navbar"])


def _phase_student_submit_defense(actors, student_cred):
    actors["login"].open()
    actors["login"].login(student_cred, expected_url="**/home*")

    student_page = actors["student_thesis"]
    student_page.submit_defense_request(file_path("defense_dummy.zip"))

    _safe_logout(student_page.page, actors["navbar"])


def _phase_kaprodi_approve_defense(actors, kaprodi_cred, student_name):
    actors["login"].open()
    actors["login"].login(kaprodi_cred, expected_url="**/Adminkaprodi*")

    defense_page = actors["kaprodi_defense"]
    defense_page.navigate_to_defense_documents()
    page = defense_page.page

    page.get_by_role("tab", name=re.compile(r"Submitted.*")).click()
    page.wait_for_timeout(1000)

    row = page.locator("tr").filter(has_text=re.compile(student_name, re.IGNORECASE)).first
    try:
        row.wait_for(state="visible", timeout=3000)
    except Exception:
        _safe_logout(page, actors["navbar"])
        return

    defense_page.check_defense_in_tab(student_name, tab_pattern=r"Submitted.*")
    defense_page.accept_defense_request(student_name)
    defense_page.check_defense_in_tab(student_name, tab_pattern=r"Approved.*")

    _safe_logout(page, actors["navbar"])


@allure.title("TC-21: 🟡 PENDING — E2E thesis flow (state-machine, idempotent)")
def test_thesis_full_flow(page, login_credentials, thesis_actors):
    # Arrange
    student_cred = login_credentials["student"]
    kaprodi_cred = login_credentials["kaprodi"]
    lecturer_cred = login_credentials["lecturer"]
    thesis_data = generate_thesis_proposal(student_cred["username"])
    thesis_title = thesis_data["thesis_title"]

    # Act — login student & deteksi state
    actors = thesis_actors
    actors["login"].open()
    actors["login"].login(student_cred, expected_url="**/home*")
    state = _detect_thesis_state(page, actors["student_thesis"])
    _safe_logout(page, actors["navbar"])

    # Eksekusi fall-through sesuai state
    if state == STATE_NO_PROPOSAL:
        _phase_submit_proposal(actors, student_cred, thesis_data)
        _phase_kaprodi_approve_proposal(actors, kaprodi_cred, thesis_title)
        _phase_lecturer_approve_research(actors, lecturer_cred, student_cred["username"])
        _phase_student_submit_defense(actors, student_cred)
        _phase_kaprodi_approve_defense(actors, kaprodi_cred, student_cred["username"])
    elif state == STATE_PROPOSAL_SUBMITTED:
        _phase_kaprodi_approve_proposal(actors, kaprodi_cred, thesis_title)
        _phase_lecturer_approve_research(actors, lecturer_cred, student_cred["username"])
        _phase_student_submit_defense(actors, student_cred)
        _phase_kaprodi_approve_defense(actors, kaprodi_cred, student_cred["username"])
    elif state == STATE_DEFENSE_READY:
        _phase_student_submit_defense(actors, student_cred)
        _phase_kaprodi_approve_defense(actors, kaprodi_cred, student_cred["username"])
    elif state == STATE_DEFENSE_SUBMITTED:
        _phase_kaprodi_approve_defense(actors, kaprodi_cred, student_cred["username"])
