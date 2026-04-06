"""
Sidebar Navigation POM for Admin Office

This module provides reusable navigation methods for the admin office sidebar.
"""

from playwright.sync_api import Page


class AdminOfficeSidebar:
    def __init__(self, page: Page):
        self.page = page

        # Main Menu Items
        self.dashboard_menu = page.get_by_text("Dashboard", exact=True)
        self.operations_menu = page.get_by_text("Operations", exact=True)
        self.master_menu = page.get_by_text("Master", exact=True)
        self.admission_menu = page.get_by_text("Admission", exact=True)

        # Operations Submenu Items
        self.operations_course_offering = page.get_by_text("Course Offering", exact=True)
        self.operations_skpi = page.get_by_text("SKPI", exact=True)
        self.operations_news = page.get_by_text("News", exact=True)
        self.operations_events = page.get_by_text("Events", exact=True)
        self.operations_approvals = page.get_by_text("Approvals", exact=True)

        # Master Submenu Items
        self.master_class = page.get_by_text("Master Class", exact=True)
        self.master_course = page.get_by_text("Master Course", exact=True)
        self.master_schedule = page.get_by_text("Master Schedule", exact=True)
        self.master_lecturer = page.get_by_text("Master Lecturer", exact=True)
        self.master_kaprodi = page.get_by_text("Master Kaprodi", exact=True)
        self.master_student = page.get_by_text("Master Student", exact=True)
        self.master_room = page.get_by_text("Master Room", exact=True)
        self.master_department = page.get_by_text("Master Department", exact=True)
        self.master_faculty = page.get_by_text("Master Faculty", exact=True)

        # Admission Submenu Items
        self.admission_candidate_list = page.get_by_text("Candidate List", exact=True)
        self.admission_payment = page.get_by_text("Payment Management", exact=True)

    def navigate_to_dashboard(self):
        """Navigate to Dashboard"""
        self.dashboard_menu.click()
        self.page.wait_for_load_state("networkidle")

    # Operations Navigation
    def navigate_to_operations_course_offering(self):
        """Navigate to Operations → Course Offering"""
        self.operations_menu.click()
        self.operations_course_offering.wait_for(state="visible")
        self.operations_course_offering.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_operations_skpi(self):
        """Navigate to Operations → SKPI"""
        self.operations_menu.click()
        self.operations_skpi.wait_for(state="visible")
        self.operations_skpi.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_operations_news(self):
        """Navigate to Operations → News"""
        self.operations_menu.click()
        self.operations_news.wait_for(state="visible")
        self.operations_news.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_operations_events(self):
        """Navigate to Operations → Events"""
        self.operations_menu.click()
        self.operations_events.wait_for(state="visible")
        self.operations_events.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_operations_approvals(self):
        """Navigate to Operations → Approvals"""
        self.operations_menu.click()
        self.operations_approvals.wait_for(state="visible")
        self.operations_approvals.click()
        self.page.wait_for_load_state("networkidle")

    # Master Navigation
    def navigate_to_master_class(self):
        """Navigate to Master → Master Class"""
        self.master_menu.click()
        self.master_class.wait_for(state="visible")
        self.master_class.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_master_course(self):
        """Navigate to Master → Master Course"""
        self.master_menu.click()
        self.master_course.wait_for(state="visible")
        self.master_course.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_master_schedule(self):
        """Navigate to Master → Master Schedule"""
        self.master_menu.click()
        self.master_schedule.wait_for(state="visible")
        self.master_schedule.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_master_lecturer(self):
        """Navigate to Master → Master Lecturer"""
        self.master_menu.click()
        self.master_lecturer.wait_for(state="visible")
        self.master_lecturer.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_master_kaprodi(self):
        """Navigate to Master → Master Kaprodi"""
        self.master_menu.click()
        self.master_kaprodi.wait_for(state="visible")
        self.master_kaprodi.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_master_student(self):
        """Navigate to Master → Master Student"""
        self.master_menu.click()
        self.master_student.wait_for(state="visible")
        self.master_student.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_master_room(self):
        """Navigate to Master → Master Room"""
        self.master_menu.click()
        self.master_room.wait_for(state="visible")
        self.master_room.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_master_department(self):
        """Navigate to Master → Master Department"""
        self.master_menu.click()
        self.master_department.wait_for(state="visible")
        self.master_department.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_master_faculty(self):
        """Navigate to Master → Master Faculty"""
        self.master_menu.click()
        self.master_faculty.wait_for(state="visible")
        self.master_faculty.click()
        self.page.wait_for_load_state("networkidle")

    # Admission Navigation
    def navigate_to_admission_candidate_list(self):
        """Navigate to Admission → Candidate List"""
        self.admission_menu.click()
        self.admission_candidate_list.wait_for(state="visible")
        self.admission_candidate_list.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_admission_payment(self):
        """Navigate to Admission → Payment Management"""
        self.admission_menu.click()
        self.admission_payment.wait_for(state="visible")
        self.admission_payment.click()
        self.page.wait_for_load_state("networkidle")
