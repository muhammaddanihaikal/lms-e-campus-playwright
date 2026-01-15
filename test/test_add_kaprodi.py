from playwright.sync_api import expect
import re
from data.login_data import LoginData
from pages.login_page import LoginPage
from pages.admin_office.master.master_kaprodi.master_kaprodi_page import MasterKaprodiPage
from data.kaprodi_data import kaprodi_data

def test_add_kaprodi(page):
    # Login admin kaprodi
    login = LoginPage(page)
    login.open()
    login.login(LoginData.adminoffice)

    # navigasi ke master kaprodi
    master_kaprodi = MasterKaprodiPage(page)
    master_kaprodi.navigate()
    
    # Wait for table
    page.wait_for_load_state('networkidle')

    # buat data kaprodi baru
    print("Adding Kaprodi...")
    data = kaprodi_data()
    print(f"Data: {data}")
    employee_id = master_kaprodi.add(data)
    print(f"===Generated Employee ID===: {employee_id}")

    # Reload untuk memastikan data terbaru (opsional, jika app butuh reload)
    page.reload()
    page.wait_for_load_state('networkidle')
    
    # Search Kaprodi
    print(f"Searching for {employee_id}...")
    page.get_by_placeholder(re.compile(r"Search", re.I)).fill(employee_id)
    
    # Assert data ada di tabel
    # This is expected to fail currently due to app bug
    expect(page.locator("tbody")).to_contain_text(employee_id)