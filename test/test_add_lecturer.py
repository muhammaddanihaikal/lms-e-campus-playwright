from pages.login_page import LoginPage
from pages.admin_office.master.master_lecturer.master_lecturer_page import MasterLecturerPage
from data.login_data import LoginData
from data.lecturer_data import lecturer_data

def test_add_lecturer(page):
    # Login sebagai Admin Office
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)
    
    # Inisialisasi halaman Master Lecturer
    master_lecturer = MasterLecturerPage(page)
    
    # Masuk ke halaman Master Lecturer
    master_lecturer.navigate()
    
    # Buat data dosen
    data = lecturer_data()
    
    # Simpan data dosen
    employee_id = master_lecturer.add(data)
    
    # Validasi (search dan pastikan muncul di tabel)
    master_lecturer.search(employee_id)
