from playwright.sync_api import Page
import re


class KaprodiApprovalPage:
    """Halaman Approval Proposal untuk Kaprodi"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Menu Navigation
        self.thesis_management = page.locator('div').filter(has_text='Thesis Management').nth(5)
        self.proposal_approval_link = page.get_by_role("link", name="Proposal Approval")
        
        # Proposal List
        self.pending_tab = page.get_by_role("tab", name=re.compile(r"Pending.*"))
        self.thesis_proposal_text = page.get_by_text("Thesis Proposal")
        
        # Proposal Detail
        self.proposal_cell = None  # Akan di-set dinamis berdasarkan nama student
        
        # Approval Action
        self.approve_btn = page.get_by_role("button", name="Approve")
        self.choose_advisor = page.get_by_label("Choose Advisor **")
        self.approval_note = page.get_by_role("textbox", name="Approval Note (Optional)")
        self.approve_proposal_btn = page.get_by_role("button", name="Approve Proposal")
    
    def navigate_to_approval(self):
        """Navigate ke halaman Proposal Approval"""
        # Klik Thesis Management 2x jika perlu (karena accordion) atau pakai wait
        self.thesis_management.click()
        self.page.wait_for_timeout(500)
        
        self.proposal_approval_link.click()
        self.page.wait_for_load_state("networkidle")
        
        # Selalu pastikan masuk ke tab Pending
        self.pending_tab.click()
        self.page.wait_for_timeout(500)
    
    def debug_proposal_list(self):
        """Debug: Print semua tab dan proposal yang tersedia"""
        # Cek semua tabs
        all_tabs = self.page.get_by_role("tab").all()
        print(f"\n=== Available Tabs ({len(all_tabs)}) ===")
        for tab in all_tabs:
            try:
                text = tab.inner_text()
                print(f"  - {text}")
            except:
                pass
        
        # Screenshot untuk reference
        self.page.screenshot(path="debug_kaprodi_approval.png")
        print("Screenshot saved: debug_kaprodi_approval.png")
    
    def find_proposal(self, student_name: str, timeout: int = 10000):
        """Cari proposal berdasarkan nama student
        
        Args:
            student_name: Nama student yang proposalnya akan diapprove
            timeout: Timeout dalam ms (default: 10000)
        """
        # Coba cari dengan nama student
        self.proposal_cell = self.page.get_by_role("cell", name=student_name)
        
        try:
            self.proposal_cell.wait_for(state="visible", timeout=timeout)
        except:
            # Jika tidak ditemukan, coba cari dengan text lain yang mirip
            # Ambil screenshot untuk debug
            self.page.screenshot(path="debug_proposal_list.png")
            
            # Coba cari semua cells
            all_cells = self.page.get_by_role("cell").all()
            print(f"\n=== Found {len(all_cells)} cells in proposal list ===")
            for i, cell in enumerate(all_cells[:10]):  # Show first 10
                try:
                    text = cell.inner_text()
                    print(f"  [{i}] {text}")
                except:
                    pass
            
            # Re-raise error
            raise Exception(f"Proposal untuk '{student_name}' tidak ditemukan. Lihat debug_proposal_list.png")
    
    def open_pending_proposal(self, thesis_title: str):
        """Buka proposal yang statusnya Pending
        
        Args:
            thesis_title: Judul thesis untuk mencari action button di baris yang tepat
        """
        # Berdasarkan codegen: klik button di dalam row yang sesuai
        # Gunakan filter agar lebih akurat daripada nth()
        row = self.page.get_by_role("row", name=thesis_title)
        
        # Klik ikon mata (button pertama di row tersebut biasanya)
        row.get_by_role("button").click()
        
        self.page.wait_for_timeout(1000)
    
    def approve_proposal(self, data: dict):
        """Approve proposal

        Args:
            data: Dictionary dengan keys:
                - advisor (str, optional): Nama advisor
                - approval_note (str, optional): Catatan approval
        """
        # Klik Approve
        self.approve_btn.click()
        self.page.wait_for_timeout(200)  # Reduced from 500

        # Pilih Advisor jika ada
        if "advisor" in data:
            self.choose_advisor.select_option(data["advisor"])
            self.page.wait_for_timeout(100)  # Reduced from 300

        # Isi Approval Note jika ada
        if "approval_note" in data:
            self.approval_note.fill(data["approval_note"])

        # Klik Approve Proposal
        self.approve_proposal_btn.click()
        self.page.wait_for_load_state("networkidle")
