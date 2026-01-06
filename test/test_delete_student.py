from pages.login_page import LoginPage
from pages.admin_office.master.master_student_page.master_student_page import MasterStudentPage
from data.login_data import LoginData
from data.add_student_data import add_student_data

def test_delete_student(page):
    # 1. Login sebagai Admin Office
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)
    
    # 2. Inisialisasi halaman Master Student
    master_student = MasterStudentPage(page)
    master_student.navigate()
    
    # 3. Buat siswa baru untuk dihapus agar test mandiri
    data = add_student_data()
    master_student.add(data)
    
    # 4. Jalankan fungsi Delete berdasarkan nama siswa yang baru dibuat
    master_student.delete(data["full_name"]) 

    # Validasi (Opsional)
    from playwright.sync_api import expect
    # Pastikan nama siswa tersebut sudah tidak ada lagi di halaman
    expect(page.get_by_text(data["full_name"])).not_to_be_visible()
