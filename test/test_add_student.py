from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_office.master.master_student_page import MasterStudentPage
from data.login_data import LoginData
from data.add_student_data import add_student_data

def test_add_student():
    with sync_playwright() as p:
        # Buka browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Login sebagai Admin Office
        login = LoginPage(page)
        login.open()
        login.login(LoginData.adminoffice)
        
        # Inisialisasi halaman Master Student
        master_student = MasterStudentPage(page)
        
        # Masuk ke halaman Master Student
        master_student.navigate()
        
        # Buat data siswa
        data = add_student_data()
        
        # Simpan data siswa
        master_student.submit(data)
        
        # Validasi kalau perlu (misal: cek pesan sukses)
        # page.pause()

        browser.close()
