from pages.login_page import LoginPage
from pages.admin_office.master.master_kaprodi.master_kaprodi_page import MasterKaprodiPage
from data.login_data import LoginData
from data.kaprodi_data import kaprodi_data
from pages.navbar_page import NavBarPage
from pages.get_email.get_email_page import GetEmailPage

def test_pendaftaran_kaprodi(page):
    # login
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)
    
    master_kaprodi = MasterKaprodiPage(page)
    master_kaprodi.navigate()

    # tambah kaprodi
    data = kaprodi_data()
    kaprodi_id = master_kaprodi.add(data)
    
    # validasi
    master_kaprodi.search(kaprodi_id)
    navbar = NavBarPage(page)

    # logout
    navbar.logout()

    # buka tab kaprodi
    get_email = GetEmailPage(page)
    get_email.open()
    get_email.open_kaprodi_tab()
    
    # verifikasi
    get_email.kaprodi.verify({
        "email": data["email"],
        "employee_id": kaprodi_id
    })

    # buat akun baru
    get_email.kaprodi.create_account({
        "username": data["username"],
        "password": data["password"],
        "confirm_password": data["password"]
    })