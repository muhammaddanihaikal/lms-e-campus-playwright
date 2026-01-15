from playwright.sync_api import Page, expect
from .components.add_lecturer_modal import AddLecturerModal

class MasterLecturerPage:
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.master_menu = page.get_by_text("Master", exact=True).first
        self.master_lecturer_menu = page.get_by_text("Master Lecturer", exact=True).first
        self.add_lecturer_btn = page.get_by_role("button", name="Add Lecturer")
        self.table = page.get_by_role("table").first
        self.search_input = page.get_by_placeholder("Search lecturers...")
        
        # components
        self.add_lecturer_modal = AddLecturerModal(self.page)
    
    def navigate(self):
        self.master_menu.wait_for(state="visible", timeout=10000)
        self.master_menu.click()
        self.master_lecturer_menu.wait_for(state="visible", timeout=5000)
        self.master_lecturer_menu.click()
        self.page.wait_for_url("**/master/lecturer")
        self.page.wait_for_load_state("networkidle")

    def add(self, data):
        self.add_lecturer_btn.click()
        self.add_lecturer_modal.lecturer_name.wait_for(state="visible")
        employee_id = self.add_lecturer_modal.fill_form(data)
        self.add_lecturer_modal.submit()
        self.add_lecturer_modal.lecturer_name.wait_for(state="hidden", timeout=10000)
        return employee_id
    
    def search(self, employee_id):
        self.search_input.clear()
        self.search_input.fill(employee_id)
        
        # verifikasi hasil search dengan timeout dinamis dari expect
        expect(self.table).to_contain_text(employee_id, timeout=10000)
