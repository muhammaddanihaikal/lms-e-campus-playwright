from playwright.sync_api import Page, expect

class StudentDetailModal:
    def __init__(self, page: Page):
        self.page = page
        self.edit_btn = page.get_by_role("button", name="Edit")
        self.delete_btn = page.get_by_role("button", name="Delete")

    def edit(self):
        self.edit_btn.click()

    def verify_details(self, data):
        # 1. Pastikan modal sudah terbuka
        self.page.wait_for_selector("text=Student Information", timeout=5000)

        def check(label, value):
            # Mencari elemen yang mengandung label, lalu mengambil value di sebelahnya atau di dalamnya
            # Kita coba cari text value-nya langsung di seluruh halaman modal
            expect(self.page.get_by_text(value, exact=False).first).to_be_visible()

        # Verifikasi Data Utama
        check("Full Name", data["full_name"])
        check("Email", data["email"])
        check("NISN", data["nisn"])
        
        # Student ID (Cukup cek kalau ada label 'Student ID')
        expect(self.page.get_by_text("Student ID").first).to_be_visible()
        
    def close(self):
        # Tutup Modal
        self.page.keyboard.press("Escape")
        # Tunggu sampai modal tertutup (text Student Information hilang)
        self.page.get_by_text("Student Information").wait_for(state="hidden")

    def delete(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.delete_btn.click()
