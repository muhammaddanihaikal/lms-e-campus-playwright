from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

from data.login_data import LoginData

def test_login_mahasiswa():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        login = LoginPage(page)
        login.open()
        login.login(LoginData.mahasiswa)


def test_login_dosen():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        login = LoginPage(page)
        login.open()
        login.login(LoginData.dosen)
        


def test_login_adminkaprodi():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        login = LoginPage(page)
        login.open()
        login.login(LoginData.adminkaprodi)
        


def test_login_adminoffice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        login = LoginPage(page)
        login.open()
        login.login(LoginData.adminoffice)
        

