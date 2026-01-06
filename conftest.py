import pytest
import sys
import os
from playwright.sync_api import sync_playwright

# Tambahkan root directory ke sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # Launch browser (headless=False agar terlihat, bisa diubah ke True)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        
        # Anda juga bisa menambahkan configurasi lain di sini
        # Misalnya viewport, zoom, dll.
        
        page = context.new_page()
        yield page
        
        browser.close()
