from playwright.sync_api import Page, expect
from .components.add_course_modal import AddCourseModal

class MasterCoursePage:
    def __init__(self, page: Page):
        self.page = page
        self.master_menu = page.get_by_text("Master", exact=True).first
        self.master_course_menu = page.get_by_text("Master Course", exact=True).first
        self.add_course_btn = page.get_by_role("button", name="Add Course")
        self.search_input = page.get_by_placeholder("Search by course code, name, or department...")
        self.table = page.get_by_role("table")
        
        # components
        self.add_course_modal = AddCourseModal(page)

    def navigate(self):
        # Using UI navigation to preserve session stae
        self.page.wait_for_load_state("networkidle")
        self.master_menu.click()
        self.master_course_menu.wait_for(state="visible")
        self.master_course_menu.click()
        self.page.wait_for_load_state("networkidle")

    def add(self, data):
        self.add_course_btn.click()
        self.add_course_modal.fill_form(data)
        self.add_course_modal.submit()

    def search_by_course_name(self, data):
        expect(self.table).to_contain_text(data["course_name"])

