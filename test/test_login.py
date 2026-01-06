from pages.login_page import LoginPage
from data.login_data import LoginData

def test_login_mahasiswa(page):
    login = LoginPage(page)
    login.open()
    login.login(LoginData.mahasiswa)

def test_login_dosen(page):
    login = LoginPage(page)
    login.open()
    login.login(LoginData.dosen)

def test_login_adminkaprodi(page):
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminkaprodi)

def test_login_adminoffice(page):
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)
