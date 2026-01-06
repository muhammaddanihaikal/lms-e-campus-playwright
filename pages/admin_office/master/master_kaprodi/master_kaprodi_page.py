from playwright.sync_api import Page, expect
from .components.add_kaprodi_modal import AddKaprodiModal

class MasterKaprodiPage:
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.master_menu = page.get_by_text("Master", exact=True).first
        self.master_kaprodi_menu = page.get_by_text("Master Kaprodi", exact=True).first
        self.add_kaprodi_btn = page.get_by_role("button", name="Add Kaprodi")
        self.table = page.get_by_role("table").first
        self.search_input = page.get_by_placeholder("Search kaprodis...")
        
        # components
        self.add_kaprodi_modal = AddKaprodiModal(self.page)
    
    def navigate(self):
        self.master_menu.wait_for(state="visible", timeout=10000)
        self.master_menu.click()
        self.master_kaprodi_menu.wait_for(state="visible", timeout=5000)
        self.master_kaprodi_menu.click()
        self.page.wait_for_url("**/master/kaprodi")
        self.page.wait_for_load_state("networkidle")

    def add(self, data):
        self.add_kaprodi_btn.click()
        self.add_kaprodi_modal.kaprodi_name.wait_for(state="visible")
        employee_id = self.add_kaprodi_modal.fill_form(data)
        self.add_kaprodi_modal.submit()
        self.add_kaprodi_modal.kaprodi_name.wait_for(state="hidden", timeout=10000)
        return employee_id
    
    def search(self, employee_id):
        self.search_input.clear()
        self.search_input.fill(employee_id)
        self.page.wait_for_timeout(1000) 
        
        # verifikasi hasil search
        expect(self.table).to_be_visible(timeout=5000)
        expect(self.table).to_contain_text(employee_id)
        