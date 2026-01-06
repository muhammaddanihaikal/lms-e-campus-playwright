from playwright.sync_api import Page, expect
from config.config import BASE_URL
from datetime import datetime
from .components.add_student_modal import AddStudentModal
from .components.edit_student_modal import EditStudentModal
from .components.student_detail_modal import StudentDetailModal

class MasterStudentPage:
    def __init__(self, page: Page):
        self.page = page

        # Components
        self.add_student_modal = AddStudentModal(page)
        self.edit_student_modal = EditStudentModal(page)
        self.student_detail_modal = StudentDetailModal(page)
        
        # Navigasi
        self.master_menu = page.get_by_text("Master", exact=True).first
        self.master_student_menu = page.get_by_text("Master Student", exact=True)
        self.add_new_student_btn = page.get_by_role("button", name="Add New Student")
        self.search_input = page.get_by_placeholder("Search students...")
    
    def navigate(self):
        self.master_menu.click()
        # Wait for submenu to appear
        self.master_student_menu.wait_for(state="visible")
        self.master_student_menu.click()
    
    def add(self, data):
        self.add_new_student_btn.click()
        # Wait for modal to appear
        self.add_student_modal.full_name.wait_for(state="visible")
        nim = self.add_student_modal.fill_form(data)
        self.add_student_modal.submit()
        return nim

    def details(self, name):
        # Cari student dulu agar muncul di tabel (menghindari masalah pagination)
        self.search_input.fill(name)
        # Klik tombol details pada row yang sesuai dengan nama student
        # Tunggu sampai row yang dicari muncul
        row = self.page.get_by_role("row", name=name)
        row.get_by_role("button", name="Details").first.wait_for(state="visible")
        row.get_by_role("button", name="Details").first.click()

    def verify_details(self, data):
        # Delegasikan verifikasi ke component modal
        self.student_detail_modal.verify_details(data)
        # Tutup modal setelah verifikasi
        self.student_detail_modal.close()

    def edit(self, name, new_data):
        # 1. Buka detail student
        self.details(name)
        # 2. Klik Edit di modal detail
        self.student_detail_modal.edit()
        # 3. Isi form edit
        self.edit_student_modal.fill_form(new_data)
        # 4. Simpan perubahan
        self.edit_student_modal.submit()
        self.page.wait_for_load_state("networkidle")

    def delete(self, name):
        # Buka detail student
        self.details(name)
        # Delegasikan aksi delete ke component modal
        self.student_detail_modal.delete()
        self.page.wait_for_load_state("networkidle")
