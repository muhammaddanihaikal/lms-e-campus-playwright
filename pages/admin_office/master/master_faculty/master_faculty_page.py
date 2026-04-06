from playwright.sync_api import Page, expect
from .components.add_faculty_modal import AddFacultyModal
from .components.edit_faculty_modal import EditFacultyModal
from .components.faculty_detail_modal import FacultyDetailModal


class MasterFacultyPage:
    """Page Object for Master Faculty page"""

    def __init__(self, page: Page):
        self.page = page

        # Components
        self.add_faculty_modal = AddFacultyModal(page)
        self.edit_faculty_modal = EditFacultyModal(page)
        self.faculty_detail_modal = FacultyDetailModal(page)

        # Import AdminOfficeSidebar for navigation
        from ...sidebar import AdminOfficeSidebar
        self.sidebar = AdminOfficeSidebar(page)

        # Main page elements
        self.add_new_faculty_btn = page.get_by_role("button", name="Add New Faculty")
        self.search_input = page.get_by_placeholder("Search faculties...")

        # Table
        self.faculty_table = page.get_by_role("table")

    def navigate(self):
        """Navigate ke halaman Master Faculty"""
        self.sidebar.navigate_to_master_faculty()

    def add(self, data: dict) -> str:
        """Tambah fakultas baru, return faculty code"""
        self.add_new_faculty_btn.click()
        self.add_faculty_modal.faculty_code.wait_for(state="visible", timeout=10000)
        faculty_code = self.add_faculty_modal.fill_form(data)
        self.add_faculty_modal.submit()
        self.page.wait_for_load_state("networkidle")
        return faculty_code

    def search(self, query: str):
        """Cari fakultas"""
        self.search_input.fill(query)

    def get_faculty_row(self, name: str):
        """Dapatkan row berdasarkan nama"""
        self.search(name)
        row = self.page.get_by_role("row", name=name)
        row.wait_for(state="visible", timeout=10000)
        return row

    def details(self, name: str):
        """Klik tombol detail fakultas"""
        row = self.get_faculty_row(name)
        row.get_by_role("button", name="Details").first.click()
        self.faculty_detail_modal.modal.wait_for(state="visible", timeout=10000)

    def verify_details(self, data: dict):
        """Verifikasi detail fakultas"""
        self.faculty_detail_modal.verify_details(data)
        self.faculty_detail_modal.close()

    def edit(self, name: str, new_data: dict):
        """Edit fakultas"""
        self.details(name)
        self.faculty_detail_modal.edit()
        self.edit_faculty_modal.fill_form(new_data)
        self.edit_faculty_modal.submit()
        self.page.wait_for_load_state("networkidle")

    def delete(self, name: str):
        """Hapus fakultas"""
        self.details(name)
        self.faculty_detail_modal.delete()
        self.page.wait_for_load_state("networkidle")

    def verify_faculty_exists(self, name: str, timeout: int = 5000) -> bool:
        """Cek apakah fakultas ada di tabel"""
        try:
            row = self.page.get_by_role("row", name=name)
            row.wait_for(state="visible", timeout=timeout)
            return True
        except:
            return False

    def verify_faculty_deleted(self, name: str, timeout: int = 5000) -> bool:
        """Cek apakah fakultas sudah dihapus"""
        try:
            row = self.page.get_by_role("row", name=name)
            row.wait_for(state="visible", timeout=timeout)
            return False  # Still exists
        except:
            return True  # Deleted
