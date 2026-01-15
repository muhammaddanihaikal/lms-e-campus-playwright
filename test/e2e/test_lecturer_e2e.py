from pages.login_page import LoginPage
from pages.admin_office.master.master_lecturer.master_lecturer_page import MasterLecturerPage
from data.login_data import LoginData
from data.lecturer_data import lecturer_data
from pages.get_email.get_email_page import GetEmailPage
from pages.navbar_page import NavBarPage

def test_add_lecturer_and_create_account(page):
    # Login sebagai Admin Office
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)
    
    # Navigasi ke menu Master Lecturer
    master_lecturer = MasterLecturerPage(page)
    master_lecturer.navigate()
    
    # tambah lecturer
    data = lecturer_data()
    employee_id = master_lecturer.add(data)
    
    # logout
    navbar = NavBarPage(page)
    navbar.logout()
    
    # buka tab lecturer di get email page
    get_email = GetEmailPage(page)
    get_email.open()
    get_email.open_lecturer_tab()
    
    # verifikasi
    get_email.lecturer.verify(
        {
            "email": data["email"], 
            "employee_id": employee_id
        }
    )
    
    # buat akun
    get_email.lecturer.create_account(
        {
            "username": data["username"],
            "password": data["password"],
            "confirm_password": data["confirm_password"]
        }
    )
    
    # Optional: Login as New Lecturer to verify
    # login.open() # usually it redirects or stays on login
    # login.login({"username": data["username"], "password": data["password"]})
    # expect(page).to_have_url("**/lecturer/dashboard") # or similar
