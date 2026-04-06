"""
Modul ini berisi Page Object untuk halaman Admission dan Approval.

Classes:
    - AdmissionPage: Halaman form pendaftaran siswa baru
    - ApprovalPage: Halaman untuk approval admission di dashboard admin
"""

from playwright.sync_api import Page
from config.config import BASE_URL


class AdmissionPage:
    """
    Page Object untuk halaman Admission (pendaftaran siswa baru).

    Fungsi utama:
    - Membuka halaman admission dari login page
    - Mengisi dan submit form admission
    """

    def __init__(self, page: Page):
        """Inisialisasi semua locator yang dibutuhkan di form admission."""
        self.page = page

        # ==========================================
        # Section 1: Data Pribadi Siswa
        # ==========================================
        self.full_name = page.locator('input[name="name"]')
        self.nisn = page.locator('input[name="nisn"]')
        self.birth_place = page.locator('input[name="birthPlace"]')
        self.birth_date = page.locator('input[name="birthDate"]')
        self.gender = page.locator('select[name="gender"]')
        self.religion = page.locator('select[name="religion"]')
        self.address = page.locator('textarea[name="address"]')
        self.email = page.locator('input[name="email"]')
        self.phone = page.locator('input[name="phone"]')

        # ==========================================
        # Section 2: Data Orang Tua / Wali
        # ==========================================
        self.parent_name = page.locator('input[name="parentName"]')
        self.parent_phone = page.locator('input[name="parentPhone"]')
        self.parent_email = page.locator('input[name="parentEmail"]')

        # ==========================================
        # Section 3: Kontak Darurat
        # ==========================================
        self.emergency_name = page.locator('input[name="emergencyContactName"]')
        self.emergency_phone = page.locator('input[name="emergencyContactPhone"]')
        self.emergency_relation = page.locator('select[name="emergencyContactRelation"]')

        # ==========================================
        # Section 4: Data Pendidikan
        # ==========================================
        self.high_school = page.locator('input[name="highSchoolName"]')
        self.graduation_year = page.locator('select[name="graduationYear"]')
        self.education_level = page.locator('select[name="previousEducationLevel"]')

        # ==========================================
        # Section 5: Pilihan Program Studi
        # ==========================================
        self.study_program = page.locator('select[name="studyProgram"]')
        self.class_type = page.locator('select[name="classType"]')
        self.entry_path = page.locator('select[name="entryPath"]')

        # ==========================================
        # Section 6: Upload Dokumen
        # ==========================================
        self.academic_transcript = page.locator('input[name="report"]')
        self.diploma = page.locator('input[name="certificate"]')
        self.national_id = page.locator('input[name="idCard"]')
        self.family_card = page.locator('input[name="familyCard"]')

        # ==========================================
        # Tombol dan Link
        # ==========================================
        self.submit_btn = page.get_by_role("button", name="Submit")
        self.admission_link = page.get_by_role("link", name="Admission")

    def open(self):
        """
        Membuka halaman admission.

        Langkah:
        1. Buka halaman login
        2. Klik link "Admission"
        3. Tunggu halaman admission selesai load
        """
        # Buka halaman login
        self.page.goto(f"{BASE_URL}/login")
        self.page.wait_for_load_state("networkidle")

        # Klik link Admission untuk masuk ke halaman pendaftaran
        self.admission_link.click()
        self.page.wait_for_load_state("networkidle")

        # Tunggu 2 detik untuk options (study program, dll) selesai di-load dari API
        self.page.wait_for_timeout(2000)

        print(f"Berhasil membuka halaman admission: {self.page.url}")

    def submit(self, data):
        """
        Mengisi semua field form dan submit admission.

        Args:
            data (dict): Dictionary berisi semua data yang diperlukan

        Langkah:
        1. Isi data pribadi
        2. Isi data orang tua/wali
        3. Isi kontak darurat
        4. Isi data pendidikan
        5. Pilih program studi
        6. Upload semua dokumen
        7. Klik tombol Submit
        """
        # =======================
        # Isi Data Pribadi
        # =======================
        self.full_name.fill(data["full_name"])
        self.nisn.fill(data["nisn"])
        self.birth_place.fill(data["place_of_birth"])
        self.birth_date.fill(data["date_of_birth"])
        self.gender.select_option(data["gender"])
        self.religion.select_option(data["religion"])
        self.address.fill(data["address"])
        self.email.fill(data["email"])
        self.phone.fill(data["phone"])

        # =======================
        # Isi Data Orang Tua/Wali
        # =======================
        self.parent_name.fill(data["parent_name"])
        self.parent_phone.fill(data["parent_phone"])
        self.parent_email.fill(data["parent_email"])

        # =======================
        # Isi Kontak Darurat
        # =======================
        self.emergency_name.fill(data["emergency_name"])
        self.emergency_phone.fill(data["emergency_phone"])
        self.emergency_relation.select_option(data["relationship"])

        # =======================
        # Isi Data Pendidikan
        # =======================
        self.high_school.fill(data["high_school"])
        self.graduation_year.select_option(data["graduation_year"])
        self.education_level.select_option(data["education_level"])

        # =======================
        # Pilih Program Studi
        # =======================
        self.study_program.select_option(data["study_program"])
        self.class_type.select_option(data["class_type"])
        self.entry_path.select_option(data["entry_path"])

        # =======================
        # Upload Dokumen
        # =======================
        self.academic_transcript.set_input_files(data["academic_transcript"])
        self.diploma.set_input_files(data["diploma"])
        self.national_id.set_input_files(data["national_id"])
        self.family_card.set_input_files(data["family_card"])

        # =======================
        # Submit Form
        # =======================
        self.submit_btn.click()

        # Tunggu response dari server
        self.page.wait_for_timeout(3000)
        print("Form admission berhasil disubmit")


class ApprovalPage:
    """
    Page Object untuk halaman Approval di dashboard Admin Office.

    Catatan: Pending Admissions sudah tampil langsung di dashboard admin,
    tidak perlu navigasi ke halaman terpisah.
    """

    def __init__(self, page: Page):
        """Inisialisasi locator untuk pending admissions."""
        self.page = page

        # Section Pending Admissions di dashboard
        self.pending_admissions_text = self.page.get_by_text("Pending Admissions")
        self.no_pending_text = self.page.get_by_text("No pending admissions")

    def open(self):
        """
        Membuka halaman dashboard Admin Office.

        Catatan: Pending Admissions sudah ada di dashboard, jadi cukup
        tunggu halaman selesai load.
        """
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)  # Extra wait untuk dynamic content
        print("Dashboard Admin Office berhasil di-load")

    def refresh(self):
        """Refresh dashboard untuk mendapatkan data terbaru."""
        self.page.reload()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)
        print("Dashboard berhasil di-refresh")

    def has_pending_admissions(self):
        """
        Cek apakah ada pending admissions di dashboard.

        Returns:
            bool: True jika ada pending admissions, False jika tidak
        """
        # Cek apakah ada teks "No pending admissions"
        no_pending_count = self.no_pending_text.count()

        # Jika teks "No pending admissions" tidak ada, berarti ada pending admissions
        return no_pending_count == 0

    def approve_admission(self, full_name):
        """
        Approve admission berdasarkan nama siswa.

        Args:
            full_name (str): Nama lengkap siswa yang akan di-approve

        Returns:
            bool: True jika berhasil di-approve, False jika tidak ditemukan
        """
        # Cari elemen dengan nama siswa
        student_element = self.page.get_by_text(full_name, exact=False)

        if student_element.count() > 0:
            # Cari tombol Approve di dekat nama siswa
            approve_btn = student_element.locator("button", has_text="Approve")
            if approve_btn.count() > 0:
                approve_btn.first.click()
                self.page.wait_for_timeout(2000)
                print(f"Berhasil approve admission untuk: {full_name}")
                return True

        print(f"Tidak ditemukan admission untuk di-approve: {full_name}")
        return False

    def reject_admission(self, full_name):
        """
        Reject admission berdasarkan nama siswa.

        Args:
            full_name (str): Nama lengkap siswa yang akan di-reject

        Returns:
            bool: True jika berhasil di-reject, False jika tidak ditemukan
        """
        # Cari elemen dengan nama siswa
        student_element = self.page.get_by_text(full_name, exact=False)

        if student_element.count() > 0:
            # Cari tombol Reject di dekat nama siswa
            reject_btn = student_element.locator("button", has_text="Reject")
            if reject_btn.count() > 0:
                reject_btn.first.click()
                self.page.wait_for_timeout(2000)
                print(f"Berhasil reject admission untuk: {full_name}")
                return True

        print(f"Tidak ditemukan admission untuk di-reject: {full_name}")
        return False
