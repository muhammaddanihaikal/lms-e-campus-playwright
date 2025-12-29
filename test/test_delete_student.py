from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_office.master.master_student_page import MasterStudentPage
from data.login_data import LoginData

def test_delete_student():
    with sync_playwright() as p:
        # Buka browser
        browser = p.chromium.launch(headless=True) # Kita pasang True supaya running di background
        page = browser.new_page()

        # 1. Login sebagai Admin Office
        login = LoginPage(page)
        login.open()
        login.login(LoginData.adminoffice)
        
        # 2. Inisialisasi halaman Master Student
        master_student = MasterStudentPage(page)
        
        # 3. Jalankan fungsi Delete
        master_student.navigate()
        
        # Contoh: Hapus siswa berdasarkan nama tertentu yang ada di list
        master_student.delete("Lala") 


        # Validasi (Opsional: beri waktu sebentar untuk melihat hasilnya sebelum close)
        page.wait_for_timeout(3000)

        browser.close()
