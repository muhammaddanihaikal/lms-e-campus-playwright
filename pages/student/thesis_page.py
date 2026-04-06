from playwright.sync_api import Page


class StudentThesisPage:
    """Halaman Thesis untuk Student"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Menu Thesis
        self.thesis_menu = page.get_by_role("button", name="Thesis Thesis")
        self.start_proposal_btn = page.get_by_role("button", name="Start Thesis Proposal")
        self.create_thesis_btn = page.get_by_role("button", name="Create Thesis & Submit")
        
        # Form Proposal
        self.thesis_track = page.get_by_label("Thesis Track*")
        self.thesis_title = page.get_by_role("textbox", name="Thesis Title")
        
        # Advisor Selection
        self.select_advisor_btn = page.get_by_text("Select primary advisor")
        self.advisor_checkbox_first = page.get_by_role("checkbox").nth(0)
        self.advisor_checkbox_second = page.get_by_role("checkbox").nth(1)
        self.advisor_done_btn = page.get_by_role("button", name="Done")
        
        # Textareas
        self.research_background = page.get_by_role("textbox", name="Research Background")
        self.research_objectives = page.get_by_role("textbox", name="Research Objectives")
        self.methodology = page.get_by_role("textbox", name="Methodology")
        
        # Upload Proposal
        self.proposal_document_btn = page.get_by_role("button", name="Proposal Document")
        
        # Submit
        self.submit_proposal_btn = page.get_by_role("button", name="Submit Proposal")
    
    def navigate_to_thesis(self):
        """Klik menu Thesis"""
        self.thesis_menu.click()
        self.page.wait_for_timeout(200)  # Reduced from 500
    
    def start_proposal(self):
        """Klik Start Thesis Proposal"""
        self.start_proposal_btn.click()
        self.page.wait_for_timeout(200)  # Reduced from 500
    
    def create_thesis(self):
        """Klik Create Thesis & Submit"""
        self.create_thesis_btn.click()
        self.page.wait_for_timeout(500)  # Reduced from 1000
    
    def fill_proposal_form(self, data: dict):
        """Isi form proposal thesis
        
        Args:
            data: Dictionary dengan keys:
                - thesis_track (str, optional) - jika None, akan pilih option pertama
                - thesis_title (str)
                - research_background (str)
                - research_objectives (str)
                - methodology (str)
        """
        # Pilih Thesis Track
        if "thesis_track" in data and data["thesis_track"]:
            self.thesis_track.select_option(data["thesis_track"])
            self.page.wait_for_timeout(200)  # Reduced from 500
        
        # Isi Thesis Title
        if "thesis_title" in data:
            self.thesis_title.fill(data["thesis_title"])
        
        # Pilih Advisor (select 2 advisors)
        self.select_advisor_btn.click()
        self.page.wait_for_timeout(200)  # Reduced from 500
        self.advisor_checkbox_first.click()
        self.page.wait_for_timeout(100)  # Reduced from 300
        self.advisor_checkbox_second.click()
        self.page.wait_for_timeout(100)  # Reduced from 300
        self.advisor_done_btn.click()
        self.page.wait_for_timeout(200)  # Reduced from 500
        
        # Isi Textareas
        if "research_background" in data:
            self.research_background.fill(data["research_background"])
        
        if "research_objectives" in data:
            self.research_objectives.fill(data["research_objectives"])
        
        if "methodology" in data:
            self.methodology.fill(data["methodology"])
    
    def upload_proposal(self, file_path: str):
        """Upload dokumen proposal"""
        import os
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File proposal tidak ditemukan: {file_path}")
        
        # Upload file
        file_input = self.page.locator('input[type="file"]').first
        file_input.set_input_files(file_path)
        self.page.wait_for_timeout(500)  # Reduced from 2000
    
    def submit_proposal(self):
        """Submit proposal thesis"""
        self.submit_proposal_btn.click()
        self.page.wait_for_load_state("networkidle")
