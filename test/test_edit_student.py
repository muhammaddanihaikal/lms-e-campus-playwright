from pages.login_page import LoginPage
from pages.admin_office.master.master_student_page.master_student_page import MasterStudentPage
from data.login_data import LoginData
from data.add_student_data import add_student_data

def test_edit_student_details(page):
    # 1. Login
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)
    
    # 2. Inisialisasi
    master_student = MasterStudentPage(page)
    master_student.navigate()
    
    # 3. Buat siswa baru untuk diedit
    data = add_student_data()
    master_student.add(data)
    
    # 4. Update data dengan nilai baru yang berbeda
    new_data = {
        "full_name": data["full_name"] + " Edited",
        "email": "edited_" + data["email"],
        "phone": "08123456789",
        "address": "Alamat baru setelah diedit komplit",
        "status": "NON-ACTIVE"
    }
    
    # 5. Jalankan proses edit (cari berdasarkan nama lama)
    master_student.edit(data["full_name"], new_data)
    
    # 6. Verifikasi perubahan di modal Detail
    # Cari berdasarkan nama baru
    master_student.details(new_data["full_name"])
    
    # Verifikasi setiap field yang berubah
    from playwright.sync_api import expect
    expect(page.get_by_text(new_data["full_name"])).to_be_visible()
    expect(page.get_by_text(new_data["email"])).to_be_visible()
    expect(page.get_by_text(new_data["address"])).to_be_visible()
    
    # Cek status NON-ACTIVE (biasanya label atau text di modal)
    expect(page.get_by_text("NON-ACTIVE")).to_be_visible()
