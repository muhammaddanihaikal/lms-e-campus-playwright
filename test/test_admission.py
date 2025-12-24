from playwright.sync_api import sync_playwright
from pages.admission_page import AdmissionPage
from data.admission_data import admission_data


def test_admission():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Buat data dummy
        data = admission_data()

        admission = AdmissionPage(page)
        admission.open()
        admission.submit(data)