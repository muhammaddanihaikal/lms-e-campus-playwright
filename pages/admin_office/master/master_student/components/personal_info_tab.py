from playwright.sync_api import Page


class PersonalInfoTab:
    """Tab Informasi Pribadi"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.full_name = page.get_by_role("textbox", name="Full Name")
        self.email = page.get_by_role("textbox", name="Email")
        self.nisn = page.get_by_role("textbox", name="NISN")
        self.gender = page.get_by_label("Gender*")
        self.religion = page.get_by_label("Religion*")
        self.date_of_birth = page.get_by_role("textbox", name="Date of Birth")
        self.place_of_birth = page.get_by_role("textbox", name="Place of Birth")
        self.phone = page.get_by_role("textbox", name="Phone Number")
        self.address = page.get_by_role("textbox", name="Address")
    
    def fill(self, data: dict, required_fields: list = None):
        """Isi form Personal Info
        
        Args:
            data: Dictionary dengan field yang akan diisi
            required_fields: List field yang wajib diisi (default: semua field)
        """
        if required_fields is None:
            required_fields = [
                "full_name", "email", "nisn", "gender", "religion",
                "date_of_birth", "place_of_birth", "phone", "address"
            ]
        
        if "full_name" in required_fields and "full_name" in data:
            self.full_name.fill(data["full_name"])
        if "email" in required_fields and "email" in data:
            self.email.fill(data["email"])
        if "nisn" in required_fields and "nisn" in data:
            self.nisn.fill(data["nisn"])
        if "gender" in required_fields and "gender" in data:
            self.gender.select_option(data["gender"])
        if "religion" in required_fields and "religion" in data:
            self.religion.select_option(data["religion"])
        if "date_of_birth" in required_fields and "date_of_birth" in data:
            self.date_of_birth.fill(data["date_of_birth"])
        if "place_of_birth" in required_fields and "place_of_birth" in data:
            self.place_of_birth.fill(data["place_of_birth"])
        if "phone" in required_fields and "phone" in data:
            self.phone.fill(data["phone"])
        if "address" in required_fields and "address" in data:
            self.address.fill(data["address"])
