from pages.login_page import LoginPage
from pages.admin_office.master.master_student.master_student_page import MasterStudentPage
from data.login_data import LoginData
from data.student_data import student_data

def test_view_student_details(page):
    # 1. Login sebagai Admin Office
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)
    
    # 2. Inisialisasi halaman Master Student
    master_student = MasterStudentPage(page)
    
    # 3. Navigasi ke halaman Master Student List
    master_student.navigate()
    
    # 4. Buat data siswa baru untuk dites
    data = student_data()
    master_student.add(data)
    
    # 5. Buka detail dan verifikasi
    master_student.details(data["full_name"])
    master_student.verify_details(data)
