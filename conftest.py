"""Root conftest — fixture global, hook screenshot saat gagal."""

import os
import sys

import allure
import pytest
from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.config import BASE_URL  # noqa: E402


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(base_url=BASE_URL)
    page = context.new_page()
    page.set_default_timeout(60000)
    page.on("dialog", lambda dialog: dialog.accept())
    yield page
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            try:
                allure.attach(
                    page.screenshot(),
                    name="screenshot-on-failure",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception:
                pass
