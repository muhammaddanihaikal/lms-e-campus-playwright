from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_office.master.master_student_page import MasterStudentPage
from data.login_data import LoginData
from data.add_student_data import add_student_data

def test_student_lifecycle_e2e():
    with sync_playwright() as p:
        # Buka browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Login sebagai Admin Office
        login = LoginPage(page)
        login.open()
        login.login(LoginData.adminoffice)
        
        master_student = MasterStudentPage(page)
        
        # 2. Flow: Tambah Siswa Baru
        master_student.navigate()
        data = add_student_data()
        master_student.add(data)
        
        # Beri jeda sebentar jika perlu untuk memastikan data masuk ke tabel
        page.wait_for_timeout(2000)
        
        # 3. Flow: Membuka Detail & Verifikasi
        master_student.details(data["full_name"])
        master_student.verify_details(data)
        
        # 4. Flow: Hapus Siswa
        master_student.delete(data["full_name"])
        

        browser.close()
