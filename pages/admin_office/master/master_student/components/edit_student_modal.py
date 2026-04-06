from playwright.sync_api import Page
from .personal_info_tab import PersonalInfoTab
from .family_emergency_tab import FamilyEmergencyTab
from .education_academic_tab import EducationAcademicTab


class EditStudentModal:
    def __init__(self, page: Page):
        self.page = page
        
        # Tab components (reuse dari add)
        self.personal_info = PersonalInfoTab(page)
        self.family_emergency = FamilyEmergencyTab(page)
        self.education_academic = EducationAcademicTab(page)
        
        # Tab buttons
        self.tab_personal = page.get_by_role("tab", name="Personal Info")
        self.tab_family = page.get_by_role("tab", name="Family & Emergency")
        self.tab_education = page.get_by_role("tab", name="Education & Academic")
        
        # Additional fields for edit mode
        self.username = page.get_by_role("textbox", name="Username")
        self.status = page.get_by_label("Status")
        
        # Save button
        self.save_btn = page.get_by_role("button", name="Save")
    
    def switch_to_personal(self):
        """Switch ke tab Personal Info"""
        self.tab_personal.click()
        self.page.wait_for_timeout(300)
    
    def switch_to_family(self):
        """Switch ke tab Family & Emergency"""
        self.tab_family.click()
        self.page.wait_for_timeout(300)
    
    def switch_to_education(self):
        """Switch ke tab Education & Academic"""
        self.tab_education.click()
        self.page.wait_for_timeout(300)
    
    def fill_form(self, data: dict):
        """Isi seluruh form edit student (hanya field yang ada di data)
        
        Args:
            data: Dictionary dengan field yang akan diupdate
        """
        # Tentukan field yang ada di data
        personal_fields = [k for k in ["full_name", "email", "nisn", "gender", "religion",
                         "date_of_birth", "place_of_birth", "phone", "address"] if k in data]
        family_fields = [k for k in ["parent_name", "parent_phone", "contact_name", 
                         "contact_phone", "relationship"] if k in data]
        education_fields = [k for k in ["high_school", "grad_year", "prev_education",
                          "department", "semester", "degree", "class_type", "entry_path"] if k in data]
        
        # Tab 1: Personal Info (+ Username)
        if personal_fields or "username" in data:
            self.switch_to_personal()
            if personal_fields:
                self.personal_info.fill(data, required_fields=personal_fields)
            if "username" in data:
                self.username.fill(data["username"])
        
        # Tab 2: Family & Emergency
        if family_fields:
            self.switch_to_family()
            self.family_emergency.fill(data, required_fields=family_fields)
        
        # Tab 3: Education & Academic (+ Status)
        if education_fields or "status" in data:
            self.switch_to_education()
            if education_fields:
                self.education_academic.fill(data, generate_nim=False, required_fields=education_fields)
            if "status" in data:
                self.status.select_option(data["status"])
    
    def submit(self):
        """Klik tombol Save"""
        self.save_btn.click()
