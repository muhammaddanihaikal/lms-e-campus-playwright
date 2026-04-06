from playwright.sync_api import Page


class EducationAcademicTab:
    """Tab Education & Academic"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Locators - Education
        self.high_school = page.get_by_role("textbox", name="High School")
        self.grad_year = page.get_by_label("Grad Year*")
        self.prev_education = page.get_by_label("Previous Education Level*")
        
        # Locators - Academic
        self.gen_btn = page.get_by_role("button", name="Gen")
        self.nim_field = page.get_by_role("textbox", name="NIM")
        self.department = page.get_by_label("Department*")
        self.semester = page.get_by_label("Semester*")
        self.degree = page.get_by_label("Degree*")
        self.class_type = page.get_by_label("Class Type")
        self.entry_path = page.get_by_label("Entry Path")
    
    def fill(self, data: dict, generate_nim: bool = True, required_fields: list = None) -> str:
        """Isi form Education & Academic
        
        Args:
            data: Dictionary dengan field yang akan diisi
            generate_nim: Apakah akan klik tombol Gen untuk generate NIM otomatis
            required_fields: List field yang wajib diisi (default: semua field)
            
        Returns:
            str: NIM yang di-generate
        """
        if required_fields is None:
            required_fields = [
                "high_school", "grad_year", "prev_education",
                "department", "semester", "degree", "class_type", "entry_path"
            ]
        
        # Education Info
        if "high_school" in required_fields and "high_school" in data:
            self.high_school.fill(data["high_school"])
        if "grad_year" in required_fields and "grad_year" in data:
            self.grad_year.select_option(data["grad_year"])
        if "prev_education" in required_fields and "prev_education" in data:
            self.prev_education.select_option(data["prev_education"])
        
        # Generate NIM jika diminta
        nim = ""
        if generate_nim:
            self.gen_btn.click()
            self.page.wait_for_timeout(500)  # Reduced from 1000
            
            # Ambil NIM yang di-generate
            try:
                nim = self.nim_field.input_value()
            except:
                pass
        
        # Academic Info
        if "department" in required_fields and "department" in data:
            self.department.select_option(data["department"])
        if "semester" in required_fields and "semester" in data:
            self.semester.select_option(data["semester"])
        if "degree" in required_fields and "degree" in data:
            self.degree.select_option(data["degree"])
        if "class_type" in required_fields and "class_type" in data:
            self.class_type.select_option(data["class_type"])
        if "entry_path" in required_fields and "entry_path" in data:
            self.entry_path.select_option(data["entry_path"])
        
        return nim
