---
name: fixture
description: Gunakan skill ini saat user meminta membuat atau memodifikasi fixture pytest — misalnya "bikin fixture untuk logged in user", "tambah fixture halaman profile", "generate fixture untuk test data", "buat conftest baru untuk module X". Juga untuk urusan setup/teardown test, login prep, atau fixture sharing antar module.
---

# Generate Fixture & Conftest

Skill untuk membuat fixture pytest mengikuti hierarki 3 level di project ini.

## Hierarki 3 Level

```
conftest.py (root)                      ← Level 1: global
  ├── browser (session scope)
  ├── page (function scope)
  └── logged_in_page (function scope)

tests/conftest.py                       ← Level 2: shared antar module
  ├── student_page
  ├── admin_page
  └── <page_object>_page

tests/<module>/conftest.py              ← Level 3: spesifik module
  ├── valid_<entity>_data
  ├── invalid_<entity>_data
  └── fixture spesifik module
```

## Aturan WAJIB

1. **Jangan tulis login langsung di test** — selalu pakai `logged_in_page` fixture.
2. **Gunakan scope yang tepat:**
   - `function` (default) — reset setiap test (untuk page, data, dll)
   - `session` — shared selama satu run (untuk browser)
3. **Naming: snake_case**, deskriptif (`valid_student_data`, bukan `data1`).
4. **Fixture yang dipakai >1 module** → taruh di `tests/conftest.py`.
5. **Fixture yang cuma dipakai 1 module** → taruh di `tests/<module>/conftest.py`.
6. **Fixture global (browser, login)** → taruh di root `conftest.py`.

## Level 1 — Root `conftest.py`

Sudah ada di project. Isinya:
- `browser` (session) — Playwright browser instance
- `page` (function) — Fresh page per test
- `logged_in_page` (function) — Pre-authenticated page
- Hook `pytest_runtest_makereport` — screenshot otomatis saat gagal

```python
# conftest.py (root)

import pytest
import os
import allure
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(base_url=os.getenv("BASE_URL"))
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="function")
def logged_in_page(page):
    """Halaman sudah login sebagai admin"""
    page.goto("/login")
    page.get_by_label("Email").fill(os.getenv("ADMIN_EMAIL"))
    page.get_by_label("Password").fill(os.getenv("ADMIN_PASSWORD"))
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/dashboard")
    return page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="screenshot-on-failure",
                attachment_type=allure.attachment_type.PNG
            )
```

## Level 2 — `tests/conftest.py` (shared antar module)

Taruh fixture Page Object yang dipakai banyak module.

```python
# tests/conftest.py

import pytest
from pages.master_student.master_student_page import MasterStudentPage


@pytest.fixture(scope="function")
def student_page(logged_in_page):
    """Halaman master student, sudah login"""
    sp = MasterStudentPage(logged_in_page)
    sp.navigate()
    return sp
```

**Pattern untuk tiap Page Object:**

```python
@pytest.fixture(scope="function")
def <nama>_page(logged_in_page):
    """<deskripsi singkat>"""
    p = <Nama>Page(logged_in_page)
    p.navigate()
    return p
```

## Level 3 — `tests/<module>/conftest.py` (spesifik module)

Taruh test data atau fixture yang cuma dipakai module ini.

```python
# tests/master_student/conftest.py

import pytest
import json


@pytest.fixture
def valid_student_data():
    with open("data/master_student/valid_student.json") as f:
        return json.load(f)


@pytest.fixture
def invalid_student_data():
    with open("data/master_student/invalid_student.json") as f:
        return json.load(f)
```

**Pattern untuk data fixture:**

```python
@pytest.fixture
def <scenario>_<entity>_data():
    with open("data/<module>/<scenario>_<entity>.json") as f:
        return json.load(f)
```

## Pattern — Fixture dengan Faker (data dinamis)

Kalau butuh data unik tiap test (misal email harus unique):

```python
# tests/<module>/conftest.py

import pytest
from utils.faker_helper import generate_student


@pytest.fixture
def random_student_data():
    """Generate data siswa random, email unique"""
    return generate_student()
```

## Pattern — Fixture dengan Cleanup (teardown)

Kalau test bikin data baru dan perlu dihapus setelahnya:

```python
@pytest.fixture
def created_student(student_page, valid_student_data):
    # Setup: bikin siswa baru
    modal = AddStudentModal(student_page.page)
    student_page.open_add_student_modal()
    modal.fill_student_form(name=valid_student_data["name"], ...)
    modal.submit()

    yield valid_student_data

    # Teardown: hapus siswa
    student_page.delete_student(valid_student_data["name"])
```

## Pattern — Parametrize Fixture

Kalau mau jalankan test untuk beberapa skenario data:

```python
@pytest.fixture(params=[
    {"role": "admin"},
    {"role": "teacher"},
    {"role": "student"},
])
def user_by_role(request):
    return request.param
```

## Workflow

1. **Tanya user**: fixture untuk apa, scope-nya (1 test / 1 module / global), data dari mana (JSON / faker / DB).
2. **Tentukan level conftest** berdasarkan scope pemakaian:
   - Dipakai 1 module saja → Level 3
   - Dipakai >1 module → Level 2
   - Browser / login global → Level 1 (jarang perlu nambah di sini)
3. **Cek apakah fixture sudah ada** — jangan buat duplikat.
4. **Generate fixture** mengikuti template di atas.
5. **Kalau butuh test data JSON** — panggil skill `test-data` untuk bikin file JSON-nya.
6. **Pastikan import-nya benar** — path relatif dari root project.

## Anti-Pattern (DILARANG)

```python
# ❌ Login di dalam test function
def test_add_student(page):
    page.goto("/login")
    page.fill(...)  # ❌ pakai logged_in_page!
    ...

# ❌ Scope salah (session untuk data test)
@pytest.fixture(scope="session")
def valid_data():  # ❌ pakai function scope, data harus fresh tiap test
    ...

# ❌ Share state antar test via fixture
_created_id = None

@pytest.fixture
def create_student_once():
    global _created_id  # ❌ anti-pattern, bikin test saling bergantung
    if _created_id is None:
        _created_id = create_student()
    return _created_id
```

## Referensi

- Full guideline: [docs/testing-guidelines.md](../../../docs/testing-guidelines.md) section 8, 13
- Test data: skill `test-data`
- Page Object: skill `pom`
