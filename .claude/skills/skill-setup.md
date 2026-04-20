---
name: setup
description: Gunakan skill ini saat user meminta setup awal project, inisialisasi module baru, atau konfigurasi environment — seperti "setup project dari awal", "tambah module test baru", "konfigurasi .env", "atur allure reporting". Juga untuk urusan CI/CD, struktur folder baru, atau saat user minta panduan memulai fitur besar yang melibatkan banyak file.
---

# QA Project Setup

Skill untuk setup project, inisialisasi module baru, dan konfigurasi environment.

## Tech Stack (wajib terinstall)

| Tool | Fungsi | Install |
|------|--------|---------|
| Playwright (Python) | Browser automation | `pip install playwright && playwright install` |
| pytest | Test runner | `pip install pytest` |
| Allure | Reporting | `pip install allure-pytest && npm i -g allure-commandline` |
| python-dotenv | Environment config | `pip install python-dotenv` |
| Faker | Data dummy | `pip install faker` |

Biasanya semua sudah di `requirements.txt` — install via:
```bash
pip install -r requirements.txt
playwright install
npm install -g allure-commandline
```

## Environment Config (`.env`)

**Aturan:**
- WAJIB simpan URL, username, password di `.env`
- **Jangan commit `.env`** — tambahkan ke `.gitignore`
- **Commit `.env.example`** sebagai template

### Template `.env`

```env
BASE_URL=https://app.example.com
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=secret123
```

### Cara pakai di kode

```python
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
```

## Struktur Folder Lengkap

```
project/
├── .env                              # Environment (jangan commit)
├── .env.example                      # Template .env (commit)
├── .gitignore
├── pytest.ini                        # Pytest config
├── requirements.txt
├── conftest.py                       # Global fixture (browser, page, login)
│
├── pages/
│   ├── base_page.py                  # Base class
│   └── <module>/
│       ├── <module>_page.py
│       └── components/
│           ├── <nama>_modal.py
│           └── tabs/
│               └── <nama>_tab.py
│
├── tests/
│   ├── conftest.py                   # Fixture shared antar module
│   └── <module>/
│       ├── conftest.py               # Fixture spesifik module
│       ├── test_add_<entity>.py
│       ├── test_edit_<entity>.py
│       └── test_delete_<entity>.py
│
├── data/
│   └── <module>/
│       ├── valid_<entity>.json
│       └── invalid_<entity>.json
│
└── utils/
    ├── faker_helper.py
    └── date_helper.py
```

## Naming Convention

| Elemen | Format | Contoh |
|--------|--------|--------|
| File | snake_case | `add_student_modal.py` |
| Class | PascalCase | `AddStudentModal` |
| Method | snake_case | `fill_student_form()` |
| Test function | snake_case + deskriptif | `test_add_student_with_valid_data()` |
| Fixture | snake_case | `student_page` |

## Workflow — Setup Module Baru

Saat user minta "tambah module test baru untuk fitur X":

1. **Bikin folder** di `pages/<module>/`, `pages/<module>/components/`, `tests/<module>/`, `data/<module>/`.
2. **Bikin Page Object** di `pages/<module>/<module>_page.py` → panggil skill `pom`.
3. **Bikin Component(s)** di `pages/<module>/components/` → panggil skill `component`.
4. **Bikin fixture module** di `tests/<module>/conftest.py` → panggil skill `fixture`.
5. **Tambah fixture page di** `tests/conftest.py` kalau dipakai module lain.
6. **Bikin test data** di `data/<module>/` → panggil skill `test-data`.
7. **Bikin test file** di `tests/<module>/test_<feature>.py` → panggil skill `test-case`.
8. **Run test**: `pytest tests/<module> -v --alluredir=allure-results`.

## Workflow — First Time Setup (dari zero)

1. **Clone repo** + `cd` ke folder.
2. **Setup Python env:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Git Bash on Windows
   pip install -r requirements.txt
   playwright install
   ```
3. **Install Allure CLI:**
   ```bash
   npm install -g allure-commandline
   ```
4. **Setup `.env`:**
   ```bash
   cp .env.example .env
   # Edit isi .env (BASE_URL, ADMIN_EMAIL, ADMIN_PASSWORD)
   ```
5. **Smoke test:**
   ```bash
   pytest tests --alluredir=allure-results
   allure serve allure-results
   ```

## CI/CD Checklist

- [ ] `headless=True` di fixture browser (pastikan di root `conftest.py`)
- [ ] `.env` di `.gitignore`
- [ ] `.env.example` di-commit dengan field lengkap
- [ ] Test command standar: `pytest tests --alluredir=allure-results`
- [ ] Screenshot otomatis saat gagal (sudah ada di hook `pytest_runtest_makereport`)
- [ ] Dependencies lengkap di `requirements.txt`

## Quick Commands

```bash
# Run semua test
pytest tests --alluredir=allure-results

# Run per module
pytest tests/authentication -v --alluredir=allure-results
pytest tests/profile -v --alluredir=allure-results
pytest tests/project -v --alluredir=allure-results

# Run single test
pytest tests/authentication/test_authentication.py::test_login_valid -v --alluredir=allure-results

# Generate + view report
allure serve allure-results
```

## Pytest Config (`pytest.ini`)

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
```

## `.gitignore` Essentials

```
# Python
__pycache__/
*.pyc
venv/
.venv/

# Environment
.env

# Test outputs
allure-results/
allure-report/
playwright-report/
test-results/
traces/

# IDE
.vscode/
.idea/
```

## Philosophy

> **Automation ≠ hanya bikin test jalan**
> **Automation = memastikan kualitas produk**

- Test harus **stabil, readable, maintainable**
- AI adalah **asisten**, bukan decision maker
- Semua perubahan penting harus melalui **review manusia**
- **Gunakan Playwright CLI** (Inspector, Codegen) untuk explore/debug locator

## Referensi

- Full guideline: [docs/testing-guidelines.md](../../../docs/testing-guidelines.md) section 1, 2, 3, 7, 15, 19
- Project-specific: [CLAUDE.md](../../../CLAUDE.md)
- Skills terkait: `generate-page-object`, `generate-component`, `generate-fixture`, `generate-test-data`, `generate-test-case`, `locator-strategy`, `debug-locator`
