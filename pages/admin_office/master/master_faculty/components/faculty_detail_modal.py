from playwright.sync_api import Page, expect


class FacultyDetailModal:
    """Modal detail fakultas"""

    def __init__(self, page: Page):
        self.page = page

        # Container modal
        self.modal = page.get_by_role("dialog").first

        # Tombol aksi
        self.edit_btn = page.get_by_role("button", name="Edit")
        self.delete_btn = page.get_by_role("button", name="Delete")
        self.close_btn = page.get_by_role("button", name="Close")

    # Ambil value dari tabel berdasarkan label
    def get_value_by_label(self, label: str):
        row = self.modal.get_by_role("row").filter(has_text=label)
        return row.get_by_role("cell").nth(1)

    # Verify data
    def verify_details(self, data: dict):
        for label, expected_value in data.items():
            actual_cell = self.get_value_by_label(label)
            expect(actual_cell).to_have_text(str(expected_value))

    def edit(self):
        """Klik tombol edit"""
        self.edit_btn.click()

    def delete(self):
        """Klik tombol hapus"""
        self.delete_btn.click()

    def close(self):
        """Klik tombol tutup"""
        self.close_btn.click()
