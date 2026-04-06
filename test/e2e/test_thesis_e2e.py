"""
E2E Test: Flow Thesis dari Student upload proposal sampai Kaprodi approve

Flow lengkap:
1. Student login → Upload proposal thesis
2. Student logout
3. Kaprodi login → Approve proposal
4. Kaprodi logout

Note: Menggunakan akun student yang sudah ada (hardaes/karenes) 
yang belum pernah submit proposal thesis.
"""
from pages.login_page import LoginPage
from pages.student.thesis_page import StudentThesisPage
from pages.kaprodi.thesis_approval_page import KaprodiApprovalPage
from pages.navbar_page import NavBarPage
from data.login_data import LoginData
from data.thesis_data import thesis_proposal_data, approval_data
import os


def test_thesis_proposal_to_approval(page):
    """
    Test flow thesis menggunakan akun student yang sudah ada.
    """
    
    # ==========================================
    # BAGIAN 1: STUDENT UPLOAD PROPOSAL
    # ==========================================
    
    # Login sebagai Student (gawates)
    print("\n=== [STUDENT] Login sebagai", LoginData.mahasiswa['username'], "===")
    login = LoginPage(page)
    login.open()
    login.login(LoginData.mahasiswa, expected_url="**/home*")
    
    # Navigate ke Thesis & Cek apakah sudah pernah submit
    print("=== [STUDENT] Check Thesis Status ===")
    student_thesis = StudentThesisPage(page)
    student_thesis.navigate_to_thesis()
    
    # Jika tombol "Start Thesis Proposal" terlihat, maka kita submit baru
    # Jika tidak, berarti sudah pernah submit (seperti gawates saat ini)
    if page.get_by_role("button", name="Start Thesis Proposal").is_visible():
        print("=== [STUDENT] Uploading New Proposal Thesis ===")
        student_thesis.start_proposal()
        student_thesis.create_thesis()
        
        # Data Thesis
        thesis_data = thesis_proposal_data(LoginData.mahasiswa['username'])
        student_thesis.fill_proposal_form(thesis_data)
        
        # Upload file proposal dari folder test/files
        dummy_file = os.path.join(os.path.dirname(__file__), "..", "files", "proposal_dummy.pdf")
        student_thesis.upload_proposal(dummy_file)
        student_thesis.submit_proposal()
        print(f"✅ [STUDENT] Proposal thesis berhasil disubmit: {thesis_data['thesis_title']}")
    else:
        print("ℹ️ [STUDENT] Proposal sudah pernah disubmit sebelumnya. Lanjut ke Approval.")
        thesis_data = thesis_proposal_data(LoginData.mahasiswa['username'])

    # Logout Student
    print("=== [STUDENT] Logout ===")
    navbar = NavBarPage(page)
    navbar.logout()
    page.wait_for_timeout(1000) # Biar logout beneran kelar
    
    # ==========================================
    # BAGIAN 2: KAPRODI APPROVE PROPOSAL
    # ==========================================
    
    # Login sebagai Kaprodi
    print("\n=== [KAPRODI] Login ===")
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminkaprodi, expected_url="**/Adminkaprodi*")
    
    # Navigate ke Approval & Approve Proposal
    print("=== [KAPRODI] Approve Proposal ===")
    kaprodi_approval = KaprodiApprovalPage(page)
    kaprodi_approval.navigate_to_approval()
    
    # Debug: lihat semua tab dan proposal
    kaprodi_approval.debug_proposal_list()
    
    # Cari proposal yang baru disubmit (gunakan thesis title)
    thesis_title = thesis_data['thesis_title']
    print(f"\n=== [KAPRODI] Mencari proposal: {thesis_title} ===")
    kaprodi_approval.find_proposal(thesis_title)
    kaprodi_approval.open_pending_proposal(thesis_title)
    
    # Approve dengan catatan
    approval = approval_data()
    kaprodi_approval.approve_proposal(approval)
    
    print("✅ [KAPRODI] Proposal berhasil diapprove")
    
    # Logout Kaprodi
    print("=== [KAPRODI] Logout ===")
    navbar = NavBarPage(page)
    navbar.logout()
    
    print("\n✅ FLOW THESIS SELESAI!")
