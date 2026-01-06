from pages.login_page import LoginPage
from pages.navbar_page import NavBarPage
from data.login_data import LoginData
from playwright.sync_api import expect

def test_logout(page):
    """
    Test logout functionality
    Flow:
    1. Login sebagai admin office
    2. Verifikasi berhasil login (ada di dashboard)
    3. Klik dropdown profile
    4. Klik logout button
    5. Verifikasi kembali ke halaman login
    """
    # 1. Login sebagai admin office
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)
    
    # 2. Verifikasi berhasil login (tunggu sampai di dashboard)
    page.wait_for_url("**/Adminoffice**")
    page.wait_for_load_state('networkidle')
    
    # 3 & 4. Logout menggunakan navbar
    navbar = NavBarPage(page)
    navbar.logout()
