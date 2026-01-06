from pages.login_page import LoginPage
from pages.admin_office.master.master_student.master_student_page import MasterStudentPage
from data.login_data import LoginData
from data.student_data import student_data
from pages.get_email.get_email_page import GetEmailPage

def test_master_student_e2e(page):
    # 1. Login sebagai Admin Office
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)
    
    master_student = MasterStudentPage(page)
    
    # 2. Flow: Tambah Siswa Baru
    master_student.navigate()
    data = student_data()
    master_student.add(data)
    
    # 3. Flow: Membuka Detail & Verifikasi
    master_student.details(data["full_name"])
    master_student.verify_details(data)
    
    # 4. Flow: Hapus Siswa
    master_student.delete(data["full_name"])
    
def test_pendaftaran_mahasiswa(page):
    # Login sebagai Admin Office
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)
    
    # Navigasi ke menu Master Student
    master_student = MasterStudentPage(page)
    master_student.navigate()
    
    # Tambah Mahasiswa Baru dan dapatkan NIM hasil generate
    data = student_data()
    student_id = master_student.add(data)
    
    # Simulasi Logout (Clear Storage & Cookies)
    page.context.clear_cookies()
    page.evaluate("window.localStorage.clear()")
    page.evaluate("window.sessionStorage.clear()")
    
    # Navigasi ke halaman Get Email
    get_email = GetEmailPage(page)
    get_email.navigate()
    
    # Verifikasi Mahasiswa menggunakan tab Student
    get_email.student.verify(data["email"], student_id)
    
    # Pembuatan Akun Kampus
    get_email.create_account(data["username"], "12345678")