from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_office.master.master_student_page import MasterStudentPage
from data.login_data import LoginData
from data.add_student_data import add_student_data

def test_view_student_details():
    with sync_playwright() as p:
        # Buka browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. Login sebagai Admin Office
        login = LoginPage(page)
        login.open()
        login.login(LoginData.adminoffice)
        
        # 2. Inisialisasi halaman Master Student
        master_student = MasterStudentPage(page)
        
        # 3. Navigasi ke halaman Master Student List
        master_student.navigate()
        
        # 4. Buat data siswa baru untuk dites
        data = add_student_data()
        master_student.add(data)
        
        # Beri jeda agar data tersimpan dan list terupdate
        page.wait_for_timeout(2000)
        
        # 5. Buka detail dan verifikasi
        master_student.details(data["full_name"])
        master_student.verify_details(data)
        

        browser.close()
