"""
Sidebar Navigation POM for Mahasiswa
"""

from playwright.sync_api import Page


class MahasiswaSidebar:
    def __init__(self, page: Page):
        self.page = page

        # Main Menu Items (on homeSelection page)
        self.lms_button = page.get_by_role("button", name="Learning Management System")
        self.myuniversity_button = page.get_by_role("button", name="My University My University")
        self.thesis_button = page.get_by_role("button", name="Thesis Thesis")

        # LMS Submenu Items (after clicking LMS)
        self.lms_dashboard = page.get_by_text("📊Dashboard")
        self.lms_course = page.get_by_text("📚Course")
        self.lms_attendance = page.get_by_text("📋Attendance")
        self.lms_schedule = page.get_by_text("🗓️Schedule")
        self.lms_gradebook = page.get_by_text("📝GradeBook")
        self.lms_assessment = page.get_by_text("📄Assessment")

        # MyUniversity Submenu Items
        self.myuniv_dashboard = page.get_by_role("link", name="🏛️ Dashboard")
        self.myuniv_announcement = page.get_by_role("link", name="📢 Announcement")
        self.myuniv_courses = page.get_by_role("link", name="📚 Courses")
        self.myuniv_student_request = page.get_by_role("link", name="📝 Student Request")
        self.myuniv_skpi = page.get_by_role("link", name="🎓 SKPI")
        self.myuniv_gradebook = page.get_by_role("link", name="📊 Gradebook")
        self.myuniv_event = page.get_by_role("link", name="🎪 Event")

        # Thesis Submenu Items
        self.thesis_dashboard = page.get_by_text("📊Dashboard")
        self.thesis_announcements = page.get_by_text("📢Announcements")
        self.thesis_hub = page.get_by_text("📚Thesis Hub")
        self.thesis_guidelines = page.get_by_text("📝Guidelines")
        self.thesis_proposal = page.get_by_text("📄Proposal")
        self.thesis_consultation = page.get_by_text("👨‍🏫Consultation")
        self.thesis_defense = page.get_by_text("🎓Defense")
        self.thesis_calendar = page.get_by_text("🗓️Calendar")

    # LMS Navigation
    def navigate_to_lms(self):
        """Navigate to Learning Management System"""
        self.lms_button.click()
        self.page.wait_for_load_state("networkidle")

    # MyUniversity Navigation
    def navigate_to_myuniversity(self):
        """Navigate to My University"""
        self.myuniversity_button.click()
        self.page.wait_for_load_state("networkidle")

    # Thesis Navigation
    def navigate_to_thesis(self):
        """Navigate to Thesis"""
        self.thesis_button.click()
        self.page.wait_for_load_state("networkidle")

    # LMS Submenu Navigation
    def lms_navigate_to_dashboard(self):
        self.navigate_to_lms()
        self.lms_dashboard.wait_for(state="visible")
        self.lms_dashboard.click()
        self.page.wait_for_load_state("networkidle")

    def lms_navigate_to_course(self):
        self.navigate_to_lms()
        self.lms_course.wait_for(state="visible")
        self.lms_course.click()
        self.page.wait_for_load_state("networkidle")

    def lms_navigate_to_attendance(self):
        self.navigate_to_lms()
        self.lms_attendance.wait_for(state="visible")
        self.lms_attendance.click()
        self.page.wait_for_load_state("networkidle")

    def lms_navigate_to_schedule(self):
        self.navigate_to_lms()
        self.lms_schedule.wait_for(state="visible")
        self.lms_schedule.click()
        self.page.wait_for_load_state("networkidle")

    def lms_navigate_to_gradebook(self):
        self.navigate_to_lms()
        self.lms_gradebook.wait_for(state="visible")
        self.lms_gradebook.click()
        self.page.wait_for_load_state("networkidle")

    def lms_navigate_to_assessment(self):
        self.navigate_to_lms()
        self.lms_assessment.wait_for(state="visible")
        self.lms_assessment.click()
        self.page.wait_for_load_state("networkidle")

    # MyUniversity Submenu Navigation
    def myuniv_navigate_to_dashboard(self):
        self.navigate_to_myuniversity()
        self.myuniv_dashboard.wait_for(state="visible")
        self.myuniv_dashboard.click()
        self.page.wait_for_load_state("networkidle")

    def myuniv_navigate_to_announcement(self):
        self.navigate_to_myuniversity()
        self.myuniv_announcement.wait_for(state="visible")
        self.myuniv_announcement.click()
        self.page.wait_for_load_state("networkidle")

    def myuniv_navigate_to_courses(self):
        self.navigate_to_myuniversity()
        self.myuniv_courses.wait_for(state="visible")
        self.myuniv_courses.click()
        self.page.wait_for_load_state("networkidle")

    def myuniv_navigate_to_student_request(self):
        self.navigate_to_myuniversity()
        self.myuniv_student_request.wait_for(state="visible")
        self.myuniv_student_request.click()
        self.page.wait_for_load_state("networkidle")

    def myuniv_navigate_to_skpi(self):
        self.navigate_to_myuniversity()
        self.myuniv_skpi.wait_for(state="visible")
        self.myuniv_skpi.click()
        self.page.wait_for_load_state("networkidle")

    def myuniv_navigate_to_gradebook(self):
        self.navigate_to_myuniversity()
        self.myuniv_gradebook.wait_for(state="visible")
        self.myuniv_gradebook.click()
        self.page.wait_for_load_state("networkidle")

    def myuniv_navigate_to_event(self):
        self.navigate_to_myuniversity()
        self.myuniv_event.wait_for(state="visible")
        self.myuniv_event.click()
        self.page.wait_for_load_state("networkidle")

    # Thesis Submenu Navigation
    def thesis_navigate_to_dashboard(self):
        self.navigate_to_thesis()
        self.thesis_dashboard.wait_for(state="visible")
        self.thesis_dashboard.click()
        self.page.wait_for_load_state("networkidle")

    def thesis_navigate_to_announcements(self):
        self.navigate_to_thesis()
        self.thesis_announcements.wait_for(state="visible")
        self.thesis_announcements.click()
        self.page.wait_for_load_state("networkidle")

    def thesis_navigate_to_hub(self):
        self.navigate_to_thesis()
        self.thesis_hub.wait_for(state="visible")
        self.thesis_hub.click()
        self.page.wait_for_load_state("networkidle")

    def thesis_navigate_to_guidelines(self):
        self.navigate_to_thesis()
        self.thesis_guidelines.wait_for(state="visible")
        self.thesis_guidelines.click()
        self.page.wait_for_load_state("networkidle")

    def thesis_navigate_to_proposal(self):
        self.navigate_to_thesis()
        self.thesis_proposal.wait_for(state="visible")
        self.thesis_proposal.click()
        self.page.wait_for_load_state("networkidle")

    def thesis_navigate_to_consultation(self):
        self.navigate_to_thesis()
        self.thesis_consultation.wait_for(state="visible")
        self.thesis_consultation.click()
        self.page.wait_for_load_state("networkidle")

    def thesis_navigate_to_defense(self):
        self.navigate_to_thesis()
        self.thesis_defense.wait_for(state="visible")
        self.thesis_defense.click()
        self.page.wait_for_load_state("networkidle")

    def thesis_navigate_to_calendar(self):
        self.navigate_to_thesis()
        self.thesis_calendar.wait_for(state="visible")
        self.thesis_calendar.click()
        self.page.wait_for_load_state("networkidle")
