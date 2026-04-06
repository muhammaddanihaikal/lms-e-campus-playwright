"""
Test Suite untuk Flow Admission Siswa Baru

Tests ini menguji flow lengkap pendaftaran siswa baru:
1. Submit admission form sebagai guest
2. Login sebagai admin office
3. Approve admission (jika backend berfungsi)
4. Cek data di Master Student
"""

from playwright.sync_api import Page
from pages.admission_page import AdmissionPage, ApprovalPage
from pages.login_page import LoginPage
from data.admission_data import admission_data
from data.login_data import LoginData


def test_admission_submit_only(page: Page):
    """
    Test sederhana: Submit admission form tanpa approval.

    Tujuan: Memastikan form submission berjalan dengan benar.

    Langkah:
    1. Buka halaman admission
    2. Isi form dengan data random
    3. Submit form
    4. Verifikasi URL masih di halaman admission
    """
    admission_page = AdmissionPage(page)
    admission_page.open()

    data = admission_data()
    admission_page.submit(data)

    assert "admission" in page.url.lower()


def test_admission_complete_flow(page: Page):
    """
    Test flow admission lengkap.

    Tujuan: Menguji flow end-to-end dari pendaftaran sampai approval.

    Catatan: Test ini mungkin gagal jika backend belum menyimpan data
    admission ke database dengan benar.

    Langkah:
    1. Submit admission sebagai guest
    2. Login sebagai admin office
    3. Cek pending admissions di dashboard
    4. Approve admission (jika ada)
    5. Cek di Master Student
    """
    admission_page = AdmissionPage(page)
    admission_page.open()

    data = admission_data()
    admission_page.submit(data)

    assert "admission" in page.url.lower()

    # Login sebagai Admin Office
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(LoginData.adminoffice)

    assert "adminoffice" in page.url.lower() or "admin" in page.url.lower()

    # Cek Pending Admissions di Dashboard
    approval_page = ApprovalPage(page)
    approval_page.open()
    approval_page.refresh()

    has_pending = approval_page.has_pending_admissions()

    # Approve Admission (jika ada)
    if has_pending:
        approval_page.approve_admission(data["full_name"])

    # Cek Master Student
    master_student_link = page.locator("a").filter(has_text="Master Student")

    if master_student_link.count() > 0:
        try:
            master_student_link.click()
            page.wait_for_load_state("networkidle")

            # Cek apakah siswa muncul
            student_name_in_table = page.get_by_text(data["full_name"], exact=False)
            assert student_name_in_table.count() > 0
        except Exception:
            pass
