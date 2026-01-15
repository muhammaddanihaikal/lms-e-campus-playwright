from pages.login_page import LoginPage
from pages.admin_office.master.master_student.master_student_page import MasterStudentPage
from data.login_data import LoginData
from data.student_data import student_data
from pages.get_email.get_email_page import GetEmailPage
from pages.navbar_page import NavBarPage

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
    
    # tambah mahasiswa
    data = student_data()
    student_id = master_student.add(data)
    
    # logout
    navbar = NavBarPage(page)
    navbar.logout()
    
    # buka tab student
    get_email = GetEmailPage(page)
    get_email.open()
    get_email.open_student_tab()
    
    # verifikasi
    get_email.student.verify(
        {
            "email": data["email"], 
            "student_id": student_id
        }
    )
    
    # buat akun
    get_email.student.create_account(
        {
            "username": data["username"],
            "password": "12345678",
            "confirm_password": "12345678"
        }
    )