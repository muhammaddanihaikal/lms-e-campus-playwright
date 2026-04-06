from playwright.sync_api import Page, expect
from .components.add_department_modal import AddDepartmentModal
from .components.edit_department_modal import EditDepartmentModal
from .components.department_detail_modal import DepartmentDetailModal


class MasterDepartmentPage:
    """Page Object for Master Department page"""

    def __init__(self, page: Page):
        self.page = page

        # Components
        self.add_department_modal = AddDepartmentModal(page)
        self.edit_department_modal = EditDepartmentModal(page)
        self.department_detail_modal = DepartmentDetailModal(page)

        # Import AdminOfficeSidebar for navigation
        from ...sidebar import AdminOfficeSidebar
        self.sidebar = AdminOfficeSidebar(page)

        # Main page elements
        self.add_new_department_btn = page.get_by_role("button", name="Add New Department")
        self.search_input = page.get_by_placeholder("Search departments...")

        # Table
        self.department_table = page.get_by_role("table")

    def navigate(self):
        """Navigate ke halaman Master Department"""
        self.sidebar.navigate_to_master_department()

    def add(self, data: dict) -> str:
        """Tambah department baru, return department code"""
        self.add_new_department_btn.click()
        self.add_department_modal.department_code.wait_for(state="visible", timeout=10000)
        department_code = self.add_department_modal.fill_form(data)
        self.add_department_modal.submit()
        self.page.wait_for_load_state("networkidle")
        return department_code

    def search(self, query: str):
        """Cari department"""
        self.search_input.fill(query)

    def get_department_row(self, name: str):
        """Dapatkan row berdasarkan nama (ambil yang pertama)"""
        self.search(name)
        row = self.page.get_by_role("row", name=name).first
        row.wait_for(state="visible", timeout=10000)
        return row

    def details(self, name: str):
        """Klik tombol detail department"""
        row = self.get_department_row(name)
        row.get_by_role("button", name="Details").first.click()
        self.department_detail_modal.modal.wait_for(state="visible", timeout=10000)

    def verify_details(self, data: dict):
        """Verifikasi detail department"""
        self.department_detail_modal.verify_details(data)
        self.department_detail_modal.close()

    def edit(self, name: str, new_data: dict):
        """Edit department"""
        self.details(name)
        self.department_detail_modal.edit()
        self.edit_department_modal.fill_form(new_data)
        self.edit_department_modal.submit()
        self.page.wait_for_load_state("networkidle")
        # Clear search untuk refresh tabel
        self.search_input.clear()

    def delete(self, name: str):
        """Hapus department"""
        self.details(name)
        self.department_detail_modal.delete()

        # Tunggu confirmation dialog muncul dan klik Yes
        self.page.wait_for_timeout(1000)

        # Cek apakah ada confirmation dialog (Yes/No/Confirm)
        try:
            yes_btn = self.page.get_by_role("button", name="Yes")
            yes_btn.wait_for(state="visible", timeout=3000)
            yes_btn.click()
        except:
            # Coba tombol Confirm
            try:
                confirm_btn = self.page.get_by_role("button", name="Confirm")
                confirm_btn.wait_for(state="visible", timeout=3000)
                confirm_btn.click()
            except:
                # Coba tombol OK
                try:
                    ok_btn = self.page.get_by_role("button", name="OK")
                    ok_btn.wait_for(state="visible", timeout=3000)
                    ok_btn.click()
                except:
                    pass  # Tidak ada confirmation dialog

        self.page.wait_for_load_state("networkidle")
        # Clear search untuk refresh tabel
        self.search_input.clear()

    def verify_department_exists(self, name: str, timeout: int = 5000) -> bool:
        """Cek apakah department ada di tabel"""
        try:
            row = self.page.get_by_role("row", name=name).first
            row.wait_for(state="visible", timeout=timeout)
            return True
        except:
            return False

    def verify_department_deleted(self, name: str, timeout: int = 5000) -> bool:
        """Cek apakah department sudah dihapus"""
        # Clear search untuk melihat semua data
        self.search_input.clear()
        try:
            row = self.page.get_by_role("row", name=name).first
            row.wait_for(state="visible", timeout=timeout)
            return False  # Still exists
        except:
            return True  # Deleted
