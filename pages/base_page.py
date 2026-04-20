"""Base class untuk semua Page Object dan Component."""

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
