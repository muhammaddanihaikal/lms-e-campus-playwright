
# 📋 PRODUCT REQUIREMENT DOCUMENT (PRD)

## Playwright Python Test Automation Framework

| **Item**        | **Keterangan**                        |
| --------------------- | ------------------------------------------- |
| **Nama Proyek** | Playwright Python Test Automation Framework |
| **Versi**       | 3.0 (Component-Based)                       |
| **Tanggal**     | 18 Januari 2026                             |
| **Status**      | Final Approved                              |

---

## 1. PENDAHULUAN

### 1.1 Tujuan

Membangun framework test automation yang **scalable**, **maintainable**, dan **reliable** menggunakan Playwright Python dengan pola arsitektur **Page Object Model (POM)** yang terintegrasi dengan **Component-Based Design**. Framework ini mendukung integrasi dengan **Allure Report** untuk pelaporan profesional dan **MCP (Model Context Protocol)** untuk debugging berbasis AI.

### 1.2 Ruang Lingkup

- Pengujian aplikasi web End-to-End (E2E).
- Support browser Chromium, Firefox, dan WebKit.
- Manajemen test data eksternal.
- Auto-cleanup artefak debugging.
- Arsitektur modular berbasis Komponen (Reusable Components).

---

## 2. STRUKTUR PROYEK

Berikut adalah struktur folder standar yang mengadopsi **Component-Based POM**:

```text
project-root/
├── .github/
│   └── workflows/           # Konfigurasi CI/CD
├── config/
│   ├── config.yaml          # Konfigurasi URL & Environment
│   └── config.py            # Loader konfigurasi
├── pages/                   # Page Object Model Classes
│   ├── __init__.py
│   ├── base_page.py         # Class induk (Parent)
│   ├── components/          # ✨ FOLDER KOMPONEN (Reusable Parts)
│   │   ├── __init__.py
│   │   ├── navbar.py        # Komponen Navigation Bar
│   │   ├── sidebar.py       # Komponen Sidebar Menu
│   │   └── modal_alert.py   # Komponen Modal/Popup
│   ├── login_page.py        # Halaman Login
│   └── dashboard_page.py    # Halaman Dashboard
├── reports/                 # Output laporan & debug
│   ├── allure-results/      # Data mentah Allure
│   ├── allure-report/       # Laporan HTML Allure
│   ├── debug/               # File sementara (auto-deleted)
│   └── archived/            # Bukti bug yang disimpan permanen
├── test_data/               # Data testing (JSON/YAML)
│   └── users.json
├── tests/                   # File Test Case
│   ├── __init__.py
│   ├── conftest.py          # Hooks & Fixtures
│   └── test_login.py        # Skenario test login
├── utils/                   # Modul bantuan
│   ├── cleanup_manager.py   # Logika pembersihan file
│   └── mcp_debugger.py      # Integrasi AI Debugging
├── .gitignore
├── pyproject.toml           # Konfigurasi Poetry
├── pytest.ini               # Konfigurasi Pytest
└── README.md
```

---

## 3. ARSITEKTUR TEKNIS

### 3.1 Technology Stack

| Komponen        | Teknologi                |
| --------------- | ------------------------ |
| Language        | Python 3.9+              |
| Automation      | Playwright Python        |
| Test Runner     | Pytest                   |
| Dependency Mgmt | Poetry                   |
| Reporting       | Allure Report            |
| Debugging       | Chrome MCP, Context7 MCP |

### 3.2 Dependencies (`pyproject.toml`)

```toml
[tool.poetry]
name = "playwright-automation-framework"
version = "3.0.0"
description = "Component-Based Test Automation Framework"
authors = ["QA Team"]

[tool.poetry.dependencies]
python = "^3.9"
playwright = "^1.40.0"
pytest = "^7.4.0"
pytest-playwright = "^0.4.0"
allure-pytest = "^2.13.0"
pyyaml = "^6.0"

[tool.poetry.group.dev.dependencies]
black = "^24.1.0"
flake8 = "^7.0.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### 3.3 Pytest Configuration (`pytest.ini`)

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v 
    --alluredir=reports/allure-results 
    --clean-alluredir
```

---

## 4. STANDAR TEKNIS KRITIS

### 4.1 Standar Penulisan Locator (Wajib Patuhi)

Gunakan locator yang berorientasi pada user (User-facing) agar tes tangguh terhadap perubahan DOM.

**Prioritas Locator:**

| Prioritas   | Metode                   | Keterangan                                          |
| ----------- | ------------------------ | --------------------------------------------------- |
| **1** | `get_by_role()`        | Prioritas Utama (Button, Link, dll)                 |
| **2** | `get_by_label()`       | Untuk input form                                    |
| **3** | `get_by_placeholder()` | Jika label tidak ada                                |
| **4** | `get_by_text()`        | Untuk elemen non-interaktif                         |
| **5** | `get_by_test_id()`     | Jika semuanya tidak memungkinkan                    |
| **6** | `locator()`            | **HANYA JIKA MENTOK** (Wajib komentar alasan) |

**Contoh Implementasi:**

```python
# ✅ BENAR
page.get_by_role("button", name="Submit").click()

# ❌ SALAH (Rapuh)
page.locator("#submit-btn").click()
```

### 4.2 Strategi Pembersihan (Cleanup Strategy)

- File debug (screenshot/trace) wajib disimpan di `reports/debug/`.
- Folder tersebut **dihapus otomatis** setiap akhir sesi test.
- Jika butuh bukti bug, pindahkan manual ke `reports/archived/`.

**Implementasi (`utils/cleanup_manager.py`):**

```python
import os
import shutil

class CleanupManager:
    DEBUG_DIR = "reports/debug"

    @staticmethod
    def clean_debug_files():
        if os.path.exists(CleanupManager.DEBUG_DIR):
            shutil.rmtree(CleanupManager.DEBUG_DIR)
            print("🧹 Debug files cleaned up.")
```

---

## 5. ARSITEKTUR COMPONENT-BASED POM

Arsitektur ini memisahkan antara **Full Page** (Halaman Penuh) dan **Component** (Bagian Kecil yang Reusable).

### 5.1 Base Page (`pages/base_page.py`)

Class induk yang mewarisi fungsionalitas dasar.

```python
from playwright.sync_api import Page, Locator
import allure

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        with allure.step(f"Navigate to {url}"):
            self.page.goto(url)

    def take_screenshot(self, name: str):
        return self.page.screenshot(path=f"reports/debug/{name}.png")
```

### 5.2 Component Object (`pages/components/navbar.py`)

Contoh komponen yang muncul di banyak halaman.

```python
from playwright.sync_api import Page, Locator

class Navbar:
    def __init__(self, page: Page):
        self.page = page
        # Locator spesifik untuk Navbar (Menggunakan Standar)
        self.logo = page.get_by_alt_text("Logo")
        self.user_profile = page.get_by_role("link", name="Profile")
        self.logout_button = page.get_by_role("button", name="Logout")

    def click_logout(self):
        self.logout_button.click()
```

### 5.3 Page Object yang Menggunakan Component (`pages/dashboard_page.py`)

Page Object tidak lagi mendefinisikan Navbar, tapi memanggil Component-nya.

```python
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.components.navbar import Navbar  # ✨ Import Component

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Inisialisasi Component di dalam Page (Composition)
        self.navbar = Navbar(page) 

    def do_logout(self):
        # Gunakan method dari component
        self.navbar.click_logout()
```

---

## 6. STANDAR PENULISAN TEST CASE

### 6.1 Format Test Case ID

- Format: `TC-[MODUL]-[NOMOR]`
- Contoh: `TC-AUTH-001`, `TC-PROD-002`

### 6.2 Contoh Implementasi Test Case

Lokasi file: `tests/test_login.py`

```python
import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@allure.feature("Authentication")
@allure.story("Login User")
class TestLogin:

    @allure.id("TC-AUTH-001")
    @allure.title("Verify Login and Logout Flow")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_logout_flow(self, page):
        """
        TC ID: TC-AUTH-001
        Scenario: User login, verify dashboard, then logout
        Expected: User successfully logs out and returns to login page
        """
        # 1. Initialize Page Objects
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)

        # 2. Step: Login
        with allure.step("Navigate to Login Page and perform login"):
            login_page.navigate("https://example.com/login")
            login_page.login("admin", "password123")

        # 3. Step: Verify Dashboard & Logout via Component
        with allure.step("Verify dashboard and perform logout"):
            # Akses Component Navbar via Dashboard Page
            dashboard_page.navbar.click_logout()
          
        # 4. Assertion
        with allure.step("Verify return to login page"):
            assert "login" in page.url
```

---

## 7. PELAPORAN (REPORTING)

### 7.1 Allure Report

Framework menggunakan **Allure** sebagai standar pelaporan.

**Perintah Eksekusi:**

```bash
# 1. Jalankan test dan generate data
poetry run pytest tests/

# 2. Buka laporan interaktif
poetry run allure serve reports/allure-results
```

### 7.2 Screenshot Otomatis Saat Gagal

Tambahkan hook berikut di `tests/conftest.py`:

```python
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
  
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
```

---

## 8. INTEGRASI AI DEBUGGING (MCP)

Framework didesain untuk bekerja sama dengan AI Agent (Claude Code) via MCP.

### 8.1 Debugging dengan Chrome MCP

Saat test gagal, AI Agent dapat:

1. Mengakses browser yang sedang berjalan.
2. Melakukan inspeksi DOM secara visual.
3. Menganalisis penyebab error secara real-time.
4. Menyarankan perbaikan locator atau logic.

### 8.2 Referensi Library dengan Context7 MCP

AI Agent menggunakan Context7 untuk memastikan:

- Kode yang digunakan sesuai dokumentasi Playwright terkini.
- Menghindari penggunaan method yang sudah deprecated.

---

## 9. RENCANA IMPLEMENTASI

| Fase        | Aktivitas                                     | Durasi |
| ----------- | --------------------------------------------- | ------ |
| **1** | Setup project (Poetry, struktur folder)       | 2 Hari |
| **2** | Implementasi Base Page & Components           | 3 Hari |
| **3** | Pembuatan Page Objects (Integrasi Components) | 5 Hari |
| **4** | Pembuatan Test Cases dengan TC ID             | 5 Hari |
| **5** | Setup Allure Report & Auto-Cleanup            | 2 Hari |
| **6** | Integrasi MCP & Final Testing                 | 3 Hari |

---

**Dokumen ini telah mencakup seluruh kebutuhan proyek:**

1. ✅ Struktur Folder (dengan Components)
2. ✅ Standar Locator
3. ✅ Strategi Cleanup
4. ✅ Arsitektur Component-Based POM
5. ✅ Standar Penulisan Test Case
6. ✅ Reporting (Allure)
7. ✅ Integrasi MCP
