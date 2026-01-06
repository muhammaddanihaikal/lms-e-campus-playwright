from playwright.sync_api import Page, expect
from config.config import BASE_URL

class NavBarPage:
    def __init__(self, page: Page):
        self.page = page
        # profile dropdown
        self.dropdown_profile = page.locator('button[aria-haspopup="menu"]').last
        self.logout_btn = page.get_by_role("menuitem", name="Sign Out")

    
    def logout(self):
        self.dropdown_profile.click()
        self.logout_btn.click()

        # verify logout
        expect(self.page).to_have_url(f"{BASE_URL}/login")