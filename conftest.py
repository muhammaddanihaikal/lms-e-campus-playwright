import pytest
import sys
import os
from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=500  # Tambah slow_mo untuk debugging
        )
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(60000)  # Increase default timeout to 60s
        page.on("dialog", lambda dialog: dialog.accept())
        yield page
        browser.close()
