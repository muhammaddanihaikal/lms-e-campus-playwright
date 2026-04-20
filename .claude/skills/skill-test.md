---
name: test
description: Gunakan skill ini saat user meminta membuat FILE test baru di folder `tests/<module>/test_<module>.py` — bukan menambah satu test case ke file existing. Termasuk permintaan seperti "generate test file untuk module X", "bikin test file di folder tests untuk fitur Y", "tambah test suite baru untuk module Z", "setup file test untuk dashboard". Skill ini menghasilkan FILE lengkap (imports + struktur + beberapa test awal). Untuk menambah satu test case saja ke file yang sudah ada, pakai skill `test-case`.
---

# Generate Test File

Skill untuk membuat **file test lengkap** di `tests/<module>/test_<module>.py`.

## Beda dengan `generate-test-case`

| Skill | Kapan pakai |
|-------|-------------|
| `generate-test` (skill ini) | Bikin FILE baru di `tests/<module>/test_<module>.py` — header, imports, struktur, beberapa test awal |
| `generate-test-case` | Tambah SATU test case ke file yang sudah ada |

## Konvensi Project — Function-based (SATU-SATUNYA STYLE)

Semua test file WAJIB function-based. Ini standard project mengikuti `docs/testing-guidelines.md`.

- **Tidak pakai class wrapper**
- Comment: `# Arrange`, `# Act`, `# Assert`
- Assertion: `expect()` dari `playwright.sync_api` (bukan `assert`)
- Locator assertion langsung di test
- Auto-wait built-in dari Playwright — tidak perlu `wait_for_load_state()` manual

> `tests/authentication/test_authentication.py` pakai class-based karena dibuat sebelum guideline difinalisasi. File itu legacy — jangan dijadikan referensi untuk file baru.

## Penomoran TC — GLOBAL (bukan per file)

⚠️ **PENTING:** Penomoran `TC-<id>` kontinyu **di seluruh project**, bukan reset per file.

Contoh:
- `tests/authentication/test_authentication.py` → TC-1 sampai TC-6
- `tests/profile/test_profile.py` → TC-7 dan seterusnya
- File baru → lanjut dari TC terakhir

**Cara cek TC terakhir:**
```bash
grep -rh "@allure.title" tests/ | grep -oE "TC-[0-9]+" | sort -V | tail -1
```

## Struktur File

```
tests/<module>/
├── test_<module>.py               # File yang dihasilkan skill ini
└── conftest.py                    # Fixture spesifik module (kalau perlu)
```

Nama file WAJIB `test_<module>.py`, satu file per module.

## Template

```python
# tests/<module>/test_<module>.py

import allure
import pytest
from playwright.sync_api import expect

from pages.<module>.<module>_page import <Module>Page
from pages.<module>.components import <Component1>, <Component2>


@allure.title("TC-<N>: 🟡 PENDING — <Deskripsi skenario positive>")
def test_<positive_scenario>(login_as_tester):
    # Arrange
    page = login_as_tester
    <module>_page = <Module>Page(page)

    # Act
    <module>_page.navigate()

    # Assert
    expect(page.get_by_role("heading", name="<Judul Halaman>")).to_be_visible()


@allure.title("TC-<N+1>: 🟡 PENDING — <Deskripsi skenario negative>")
def test_<negative_scenario>(login_as_tester):
    # Arrange
    page = login_as_tester
    <module>_page = <Module>Page(page)

    # Act
    <module>_page.navigate()
    <aksi yang memicu error>

    # Assert
    expect(page.get_by_text("<pesan error>")).to_be_visible()


@allure.title("TC-<N+2>: ⏭️ SKIPPED — <Deskripsi>")
@pytest.mark.skip(reason="<alasan jelas>")
def test_<skipped_scenario>(login_as_tester):
    # Arrange
    page = login_as_tester

    # Act
    ...

    # Assert
    ...
```

## Contoh Lengkap (Profile Module)

```python
# tests/profile/test_profile.py

import re

import allure
import pytest
from playwright.sync_api import expect

from pages.profile.components import NotificationsTab, ProfileInfoTab, SecurityTab
from pages.profile.profile_page import ProfilePage


@allure.title("TC-7: 🟢 PASSED — Melihat halaman Profile")
def test_view_profile_page(login_as_tester):
    # Arrange
    page = login_as_tester
    profile_page = ProfilePage(page)

    # Act
    profile_page.open_via_sidebar()

    # Assert
    expect(page).to_have_url(re.compile(r".*/profile"))
    expect(page.get_by_role("heading", name="Profile Information")).to_be_visible()
    expect(page.get_by_role("tab", name="Profile")).to_be_visible()
    expect(page.get_by_role("tab", name="Security")).to_be_visible()


@allure.title("TC-8: 🟢 PASSED — Mengubah nama profile (lalu dikembalikan)")
def test_edit_profile_name(login_as_tester):
    # Arrange
    page = login_as_tester
    profile_page = ProfilePage(page)
    profile_info = ProfileInfoTab(page)

    profile_page.navigate()
    original_name = page.get_by_label("Name").input_value()

    # Act
    profile_info.edit_name("Nama Baru")

    # Assert
    expect(page.get_by_text("berhasil")).to_be_visible()

    # Teardown (kembalikan data)
    profile_info.edit_name(original_name)
```

## Aturan WAJIB

1. **Nama file** = `test_<module>.py` (match nama folder `tests/<module>/`).
2. **Penomoran TC global** — JANGAN reset dari TC-1, lanjutkan dari TC terakhir di project.
3. **Setiap test wajib `@allure.title`** dengan format `"TC-<id>: <status-emoji> — <deskripsi>"`.
4. **Status emoji awal** = `🟡 PENDING` (update ke `🟢 PASSED` setelah test lolos).
5. **Gunakan `expect()`, bukan `assert`** — auto-retry, error message lebih jelas.
6. **Jangan `wait_for_load_state()` manual** — `expect()` sudah auto-wait.
7. **Coverage minimal**: 1 positive + 1 negative per fitur utama.

## Prasyarat (WAJIB cek dulu)

1. **Page Object** di `pages/<module>/<module>_page.py` — jika belum, panggil skill `pom`
2. **Component(s)** di `pages/<module>/components/` jika test butuh interaksi modal/tab — panggil skill `component`
3. **Fixture** `login_as_tester` sudah ada di root `conftest.py`. Fixture tambahan → cek `tests/conftest.py`. Jika belum ada, panggil skill `fixture`
4. **Test data** kalau perlu → panggil skill `test-data`

## Workflow

1. **Tanya user**: module apa, skenario apa saja (minimal positive + negative).
2. **Cek prasyarat** (Page Object, Component, Fixture sudah ada?).
3. **Cari TC ID terakhir**:
   ```bash
   grep -rh "@allure.title" tests/ | grep -oE "TC-[0-9]+" | sort -V | tail -1
   ```
4. **Generate file** pakai template di atas, TC ID lanjut dari hasil grep.
5. **Run test** (pilih salah satu):
   ```bash
   # Option A: Run test saja
   pytest tests/<module>/test_<module>.py -v --alluredir=allure-results
   
   # Option B: Run test + langsung buka Allure report (pakai skill `test-report`)
   pytest tests/<module>/test_<module>.py -v --alluredir=allure-results && allure serve allure-results
   ```
   > Untuk run + report otomatis, gunakan skill `test-report` saja (lebih praktis).

6. **Update status emoji** (`🟡 PENDING` → `🟢 PASSED` / `❌ BLOCKED`).

## Anti-Pattern (DILARANG)

```python
# ❌ Class wrapper
class TestProfile:
    def test_something(self, page): ...

# ❌ assert biasa — pakai expect()
assert page.is_visible(".dashboard")

# ❌ wait_for_load_state — pakai expect()
page.wait_for_load_state("networkidle")
expect(page.get_by_role("heading")).to_be_visible()  # ✅

# ❌ Reset TC per file
# File baru mulai dari TC-1 ❌ — harus lanjut dari TC terakhir global

# ❌ Login langsung di test
def test_something(page):
    page.goto("/login")  # ❌ pakai login_as_tester

# ❌ time.sleep
time.sleep(2)  # ❌
```

## Referensi

- Full guideline: [docs/testing-guidelines.md](../../../docs/testing-guidelines.md) section 9-14, 17
- Tambah 1 test case ke file existing: skill `test-case`
- Run test + buka Allure report: skill `test-report`
- Page Object / Component: skill `pom`, `component`
- Fixture: skill `fixture`
- Locator: skill `locator`
