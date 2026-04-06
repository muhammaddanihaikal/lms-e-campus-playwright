from playwright.sync_api import Page


class FamilyEmergencyTab:
    """Tab Family & Emergency"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Locators - Family
        self.parent_name = page.get_by_role("textbox", name="Parent Name")
        self.parent_phone = page.get_by_role("textbox", name="Parent Phone")
        
        # Locators - Emergency Contact
        self.contact_name = page.get_by_role("textbox", name="Contact Name")
        self.contact_phone = page.get_by_role("textbox", name="Contact Phone")
        self.relationship = page.get_by_label("Relationship*")
    
    def fill(self, data: dict, required_fields: list = None):
        """Isi form Family & Emergency
        
        Args:
            data: Dictionary dengan field yang akan diisi
            required_fields: List field yang wajib diisi (default: semua field)
        """
        if required_fields is None:
            required_fields = [
                "parent_name", "parent_phone", "contact_name", 
                "contact_phone", "relationship"
            ]
        
        # Family Info
        if "parent_name" in required_fields and "parent_name" in data:
            self.parent_name.fill(data["parent_name"])
        if "parent_phone" in required_fields and "parent_phone" in data:
            self.parent_phone.fill(data["parent_phone"])
        
        # Emergency Contact
        if "contact_name" in required_fields and "contact_name" in data:
            self.contact_name.fill(data["contact_name"])
        if "contact_phone" in required_fields and "contact_phone" in data:
            self.contact_phone.fill(data["contact_phone"])
        if "relationship" in required_fields and "relationship" in data:
            self.relationship.select_option(data["relationship"])
