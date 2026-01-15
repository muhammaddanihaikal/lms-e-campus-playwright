from playwright.sync_api import Page
import re

class AddCourseModal:
    def __init__(self, page: Page):
        self.page = page
        
        # basic information
        self.course_name = page.get_by_role("textbox", name="Course Name")
        self.course_code = page.get_by_role("textbox", name="Course Code")
        self.course_description = page.get_by_role("textbox", name="Course Description")

        # academic information
        self.faculty = page.get_by_label("Faculty")
        self.department = page.get_by_label("Department")
        self.semester = page.get_by_label("Semester")
        self.credits = page.get_by_role("spinbutton", name="Credits")
        self.status = page.get_by_label("Status")

        # assessment indicators
        self.add_indicator_btn = page.get_by_role("button", name="Add Indicator")
        self.indicator_name = page.get_by_label("Indicator Name")
        self.indicator_weight = page.get_by_role("spinbutton", name="Weight (%)")
        self.total_weight_value = page.get_by_text("Total Weight:").locator("xpath=following-sibling::span")

        # learning outcomes
        self.add_learning_outcome_btn = page.get_by_role("button", name="Add Learning Outcome")
        self.learning_outcome = page.get_by_role("textbox", name="Describe what students will")

        # textbooks & references
        self.add_textbook_btn = page.get_by_role("button", name="Add Textbook")
        self.textbook_title = page.get_by_role("textbox", name="Book Title")
        self.textbook_author = page.get_by_role("textbox", name="Author(s)")
        self.textbook_publisher = page.get_by_role("textbox", name="Publisher")
        self.textbook_year = page.get_by_role("textbox", name="Year")

        # teaching strategies
        self.add_strategy_btn = page.get_by_role("button", name="Add Strategy")
        self.strategy = page.get_by_role("textbox", name="e.g., Lecture, Discussion,")

        # prerequisites
        self.add_prerequisite_btn = page.get_by_role("button", name="Add Prerequisite")
        self.prerequisite = page.get_by_role("textbox", name="e.g., MATH101, CS101")

        # contact & office hours
        self.contact_email = page.get_by_role("textbox", name="Contact Email")
        self.office_hours = page.get_by_role("textbox", name="Office Hours")

        # course policies
        self.attendance_policy = page.get_by_role('textbox', name='Attendance Policy')
        self.late_submission_policy = page.get_by_role('textbox', name='Late Submission Policy')
        self.academic_integrity = page.get_by_role('textbox', name='Academic Integrity')
        self.communication_policy = page.get_by_role('textbox', name='Communication Policy')

        # button save course
        self.save_course_btn = page.get_by_role("button", name="Save Course")

    def fill_form(self, data):
        # basic information
        self.course_name.fill(data["course_name"])
        self.course_description.fill(data["course_description"])
        
        # academic information
        self.faculty.select_option(label=data["faculty"])
        self.department.select_option(label=data["department"])
        self.semester.select_option(label=data["semester"])
        self.status.select_option(label=data["status"])
        
        # assessment indicators
        self.add_indicator_btn.click()
        self.indicator_name.select_option(label=data["indicator_name"])
        self.indicator_weight.fill(data["indicator_weight"])
        
        # learning outcomes
        self.add_learning_outcome_btn.click()
        self.learning_outcome.fill(data["learning_outcome"])
        
        # textbooks & references
        self.add_textbook_btn.click()
        self.textbook_title.fill(data["textbook_title"])
        self.textbook_author.fill(data["textbook_author"])
        self.textbook_publisher.fill(data["textbook_publisher"])
        self.textbook_year.fill(data["textbook_year"])
        
        # teaching strategies
        self.add_strategy_btn.click()
        self.strategy.fill(data["strategy"])
        
        # prerequisites
        self.add_prerequisite_btn.click()
        self.prerequisite.fill(data["prerequisite"])
        
        # contact & office hours
        self.contact_email.fill(data["contact_email"])
        self.office_hours.fill(data["office_hours"])

        # course policies
        self.attendance_policy.fill(data["attendance_policy"])
        self.late_submission_policy.fill(data["late_submission_policy"])
        self.academic_integrity.fill(data["academic_integrity"])
        self.communication_policy.fill(data["communication_policy"])

    def submit(self):
        self.save_course_btn.click()
