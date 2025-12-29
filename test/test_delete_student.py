from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_office.master.master_student_page import MasterStudentPage
from data.login_data import LoginData

def test_delete_student():
    with sync_playwright() as p:
        # Buka browser
        browser = p.chromium.launch(headless=False) # Kita pasang False supaya bisa lihat prosesnya
        page = browser.new_page()

        # 1. Login sebagai Admin Office
        login = LoginPage(page)
        login.open()
        login.login(LoginData.adminoffice)
        
        # 2. Inisialisasi halaman Master Student
        master_student = MasterStudentPage(page)
        
        # 3. Jalankan fungsi Delete
        # Ini akan otomatis navigasi, klik details, dan accept dialog OK
        print("Memulai proses hapus siswa...")
        master_student.delete_first_student()
        print("Proses hapus selesai.")

        # Validasi (Opsional: beri waktu sebentar untuk melihat hasilnya sebelum close)
        page.wait_for_timeout(3000)

        browser.close()
