"""Test suite Navbar admin office: dropdown profile + logout."""

import re

import allure
from playwright.sync_api import expect

from pages.navbar_page import NavBarPage


@allure.title("TC-15: 🟡 PENDING — Logout admin office via navbar profile dropdown")
def test_navbar_logout(logged_in_as_admin_office):
    # Arrange
    page = logged_in_as_admin_office
    navbar = NavBarPage(page)

    # Act
    navbar.logout()

    # Assert
    expect(page).to_have_url(re.compile(r".*login.*"))
