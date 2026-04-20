"""KaprodiSidebar — komponen sidebar navigasi role Kaprodi."""

from playwright.sync_api import Page

from pages.base_page import BasePage


class KaprodiSidebar(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Main Menu Items
        self.dashboard_menu = page.get_by_text("Dashboard", exact=True)
        self.master_menu = page.get_by_text("Master", exact=True)

        # Master Submenu Items
        self.master_student_menu = page.get_by_text("Master Student", exact=True)
        self.master_course_menu = page.get_by_text("Master Course", exact=True)

    def navigate_to_dashboard(self):
        """Navigate to Dashboard"""
        self.dashboard_menu.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_master_student(self):
        """Navigate to Master Student"""
        self.master_menu.click()
        self.master_student_menu.wait_for(state="visible")
        self.master_student_menu.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_master_course(self):
        """Navigate to Master Course"""
        self.master_menu.click()
        self.master_course_menu.wait_for(state="visible")
        self.master_course_menu.click()
        self.page.wait_for_load_state("networkidle")
