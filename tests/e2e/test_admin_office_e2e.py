"""E2E Test: Admin Office complete student management journey.

Flow: Login → add student → verify → edit → delete (complete CRUD cycle).
"""

import allure
from playwright.sync_api import expect

from utils.faker_helper import generate_student


@allure.title("TC-25: 🟡 PENDING — Admin Office E2E: CRUD student (add/view/edit/delete)")
def test_admin_office_student_crud_journey(admin_office_e2e_actors, login_credentials):
    # Arrange
    actors = admin_office_e2e_actors
    page = actors["login"].page
    admin_cred = login_credentials["admin_office"]
    student_data = generate_student()

    # Act — Login
    actors["login"].open()
    actors["login"].login(admin_cred, expected_url="**/Adminoffice**")

    # Navigate ke Master Student
    student_page = actors["student"]
    student_page.navigate()

    # 1. ADD student
    nim = student_page.add(student_data)

    # 2. VIEW student details
    student_page.details(student_data["full_name"])
    student_page.verify_details(student_data)

    # 3. EDIT student
    new_data = {
        "full_name": student_data["full_name"] + " Updated",
        "email": "updated_" + student_data["email"],
        "phone": "08999999999",
        "address": "Alamat baru setelah diedit via E2E",
    }
    student_page.edit(student_data["full_name"], new_data)
    page.wait_for_load_state("networkidle")

    # Verify edit
    student_page.details(new_data["full_name"])
    expect(page.get_by_text(new_data["email"]).first).to_be_visible()

    # 4. DELETE student
    student_page.delete(new_data["full_name"])
    page.wait_for_load_state("networkidle")

    # Assert — student hilang dari tabel
    expect(page.get_by_text(new_data["full_name"])).not_to_be_visible()

    # Logout
    actors["navbar"].logout()
    expect(page).to_have_url("**/login*")
