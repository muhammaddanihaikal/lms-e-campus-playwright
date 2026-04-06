from playwright.sync_api import Page
from .personal_info_tab import PersonalInfoTab
from .family_emergency_tab import FamilyEmergencyTab
from .education_academic_tab import EducationAcademicTab


class AddStudentModal:
    def __init__(self, page: Page):
        self.page = page
        
        # Tab components
        self.personal_info = PersonalInfoTab(page)
        self.family_emergency = FamilyEmergencyTab(page)
        self.education_academic = EducationAcademicTab(page)
        
        # Tab buttons
        self.tab_personal = page.get_by_role("tab", name="Personal Info")
        self.tab_family = page.get_by_role("tab", name="Family & Emergency")
        self.tab_education = page.get_by_role("tab", name="Education & Academic")
        
        # Save button
        self.save_btn = page.get_by_role("button", name="Save")
    
    def switch_to_personal(self):
        """Switch ke tab Personal Info"""
        self.tab_personal.click()
        self.page.wait_for_timeout(100)  # Reduced from 300

    def switch_to_family(self):
        """Switch ke tab Family & Emergency"""
        self.tab_family.click()
        self.page.wait_for_timeout(100)  # Reduced from 300

    def switch_to_education(self):
        """Switch ke tab Education & Academic"""
        self.tab_education.click()
        self.page.wait_for_timeout(100)  # Reduced from 300
    
    def fill_form(self, data: dict) -> str:
        """Isi seluruh form student baru
        
        Args:
            data: Dictionary dengan semua field student
            
        Returns:
            str: NIM yang di-generate
        """
        # Tab 1: Personal Info
        self.switch_to_personal()
        self.personal_info.fill(data)
        
        # Tab 2: Family & Emergency
        self.switch_to_family()
        self.family_emergency.fill(data)
        
        # Tab 3: Education & Academic
        self.switch_to_education()
        nim = self.education_academic.fill(data)
        
        return nim
    
    def submit(self):
        """Klik tombol Save"""
        self.save_btn.click()
