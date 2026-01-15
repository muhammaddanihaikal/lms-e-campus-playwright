from pages.login_page import LoginPage
from pages.admin_office.master.master_student.master_student_page import MasterStudentPage
from data.login_data import LoginData
from data.student_data import student_data

def test_add_student(page):
    # Login sebagai Admin Office
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)
    
    # Inisialisasi halaman Master Student
    master_student = MasterStudentPage(page)
    
    # Masuk ke halaman Master Student
    master_student.navigate()
    
    # Buat data siswa
    data = student_data()
    
    # Simpan data siswa
    master_student.add(data)
    
    # Validasi kalau perlu (misal: cek pesan sukses)
    # page.pause()
