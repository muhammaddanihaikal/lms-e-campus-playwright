"""Test suite Authentication: login per role + logout."""

import re

import allure
from playwright.sync_api import expect

from pages.authentication.components import LoginForm
from pages.login_page import LoginPage
from pages.navbar_page import NavBarPage


@allure.title("TC-1: 🟡 PENDING — Login sebagai admin office dengan kredensial valid")
def test_login_admin_office(page, valid_login_data):
    # Arrange
    login_page = LoginPage(page)
    form = LoginForm(page)

    # Act
    login_page.navigate()
    form.fill_credentials(
        valid_login_data["admin_office"]["username"],
        valid_login_data["admin_office"]["password"],
    )
    form.submit()

    # Assert
    expect(page).to_have_url(re.compile(r".*Adminoffice.*"))


@allure.title("TC-2: 🟡 PENDING — Login sebagai mahasiswa dengan kredensial valid")
def test_login_student(page, valid_login_data):
    # Arrange
    login_page = LoginPage(page)
    form = LoginForm(page)

    # Act
    login_page.navigate()
    form.fill_credentials(
        valid_login_data["student"]["username"],
        valid_login_data["student"]["password"],
    )
    form.submit()

    # Assert
    expect(page).to_have_url(re.compile(r".*home.*"))


@allure.title("TC-3: 🟡 PENDING — Login sebagai dosen dengan kredensial valid")
def test_login_lecturer(page, valid_login_data):
    # Arrange
    login_page = LoginPage(page)
    form = LoginForm(page)

    # Act
    login_page.navigate()
    form.fill_credentials(
        valid_login_data["lecturer"]["username"],
        valid_login_data["lecturer"]["password"],
    )
    form.submit()

    # Assert
    expect(page).to_have_url(re.compile(r".*E-Campus.*"))


@allure.title("TC-4: 🟡 PENDING — Login sebagai kaprodi dengan kredensial valid")
def test_login_kaprodi(page, valid_login_data):
    # Arrange
    login_page = LoginPage(page)
    form = LoginForm(page)

    # Act
    login_page.navigate()
    form.fill_credentials(
        valid_login_data["kaprodi"]["username"],
        valid_login_data["kaprodi"]["password"],
    )
    form.submit()

    # Assert
    expect(page).to_have_url(re.compile(r".*Adminkaprodi.*"))


@allure.title("TC-5: 🟡 PENDING — Logout dari dashboard admin office")
def test_logout_admin_office(logged_in_as_admin_office):
    # Arrange
    page = logged_in_as_admin_office
    navbar = NavBarPage(page)

    # Act
    navbar.logout()

    # Assert
    expect(page).to_have_url(re.compile(r".*login.*"))
