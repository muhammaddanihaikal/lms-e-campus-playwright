from playwright.sync_api import Page, expect
from config.config import BASE_URL
from .components.student_tab import StudentTab
from .components.lecturer_tab import LecturerTab
from .components.kaprodi_tab import KaprodiTab

class GetEmailPage:
    def __init__(self, page: Page):
        self.page = page
        self.get_your_email_btn = page.get_by_role("link", name="Get Your Email")

        # tabs
        self.student_tab_btn = page.get_by_role("tab", name="Student")
        self.lecturer_tab_btn = page.get_by_role("tab", name="Lecturer")
        self.kaprodi_tab_btn = page.get_by_role("tab", name="Kaprodi")

        # objects
        self.student = StudentTab(self.page)
        self.lecturer = LecturerTab(self.page)
        self.kaprodi = KaprodiTab(self.page)
        
    def open(self):
        self.get_your_email_btn.click()
    
    def open_student_tab(self):
        self.student_tab_btn.click()
    
    def open_lecturer_tab(self):
        self.lecturer_tab_btn.click()
    
    def open_kaprodi_tab(self):
        self.kaprodi_tab_btn.click()