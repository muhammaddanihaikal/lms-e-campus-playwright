"""ProposalForm — modal/form pengisian proposal thesis student."""

import os

from pages.base_page import BasePage


class ProposalForm(BasePage):

    def fill(self, data: dict):
        if data.get("thesis_track"):
            self.page.get_by_label("Thesis Track*").select_option(data["thesis_track"])
            self.page.wait_for_timeout(200)

        if "thesis_title" in data:
            self.page.get_by_role("textbox", name="Thesis Title").fill(data["thesis_title"])

        # Pilih 2 advisor
        self.page.get_by_text("Select primary advisor").click()
        self.page.wait_for_timeout(200)
        self.page.get_by_role("checkbox").nth(0).click()
        self.page.wait_for_timeout(100)
        self.page.get_by_role("checkbox").nth(1).click()
        self.page.wait_for_timeout(100)
        self.page.get_by_role("button", name="Done").click()
        self.page.wait_for_timeout(200)

        if "research_background" in data:
            self.page.get_by_role("textbox", name="Research Background").fill(data["research_background"])
        if "research_objectives" in data:
            self.page.get_by_role("textbox", name="Research Objectives").fill(data["research_objectives"])
        if "methodology" in data:
            self.page.get_by_role("textbox", name="Methodology").fill(data["methodology"])

    def upload(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File proposal tidak ditemukan: {file_path}")
        self.page.locator('input[type="file"]').first.set_input_files(file_path)
        self.page.wait_for_timeout(500)

    def submit(self):
        self.page.get_by_role("button", name="Submit Proposal").click()
        self.page.wait_for_load_state("networkidle")
