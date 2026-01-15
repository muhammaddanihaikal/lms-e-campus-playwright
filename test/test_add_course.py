from pages.login_page import LoginPage
from pages.admin_office.master.master_course.master_course_page import MasterCoursePage
from data.login_data import LoginData
from data.course_data import course_data

def test_add_course(page):
    # Login as Admin Office
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)
    
    # Navigate to Master Course
    master_course = MasterCoursePage(page)
    master_course.navigate()
    
    # Generate data
    data = course_data()
    
    # Add Course
    master_course.add(data)
    
    # Search and verify
    master_course.search_by_course_name(data)
