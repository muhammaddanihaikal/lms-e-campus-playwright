---
name: component
description: Gunakan skill ini saat user meminta membuat Component baru — modal, tab, section, atau bagian halaman yang reusable. Termasuk permintaan seperti "bikin component untuk add student modal", "generate modal edit profile", "buatkan tab personal info", "tambah section filter". Component berisi aksi detail seperti fill form, click, pilih dropdown — berbeda dengan Page yang hanya untuk navigasi.
---

# Generate Component

Skill untuk membuat **Component** (modal/tab/section) mengikuti pattern POM project ini.

## Konsep Hierarki

```
BasePage
  └── Page
        └── Component (modal, tab, section)  ← SKILL INI
              └── Aksi detail (fill, click, submit, close)
```

## Aturan WAJIB

1. **Wajib extend `BasePage`** — bukan extend `Page`. Component dan Page sejajar, sama-sama anak BasePage.
2. **Component berisi aksi detail** — fill form, click button, pilih dropdown, submit, close, dll.
3. **Harus reusable** — satu component untuk satu modal/tab/section, jangan digabung.
4. **JANGAN** ada assertion di Component — assertion hanya di test function.
5. **JANGAN** ada navigasi (`page.goto`) di Component — itu tugas Page.
6. **Naming:**
   - File: `<nama>_modal.py`, `<nama>_tab.py`, `<nama>_section.py`
   - Class: `<Nama>Modal`, `<Nama>Tab`, `<Nama>Section`
   - Method: snake_case deskriptif (`fill_student_form`, `submit`, `close`)

## Struktur Folder

```
pages/<module>/
├── <module>_page.py
└── components/
    ├── add_<entity>_modal.py
    ├── edit_<entity>_modal.py
    ├── delete_<entity>_modal.py
    └── tabs/
        ├── <nama>_tab.py
        └── <nama>_tab.py
```

## Template — Modal

```python
# pages/<module>/components/<nama>_modal.py

from pages.base_page import BasePage


class <Nama>Modal(BasePage):

    def fill_<form_name>(self, <param1>: str, <param2>: str):
        self.page.get_by_label("<Label Field 1>").fill(<param1>)
        self.page.get_by_label("<Label Field 2>").fill(<param2>)

    def submit(self):
        self.page.get_by_role("button", name="Simpan").click()

    def close(self):
        self.page.get_by_role("button", name="Batal").click()
```

## Contoh Lengkap — Add Student Modal

```python
# pages/master_student/components/add_student_modal.py

from pages.base_page import BasePage


class AddStudentModal(BasePage):

    def fill_student_form(self, name: str, email: str, phone: str = None):
        self.page.get_by_label("Nama").fill(name)
        self.page.get_by_label("Email").fill(email)
        if phone:
            self.page.get_by_label("Nomor Telepon").fill(phone)

    def select_class(self, class_name: str):
        self.page.get_by_label("Kelas").click()
        self.page.get_by_role("option", name=class_name).click()

    def submit(self):
        self.page.get_by_role("button", name="Simpan").click()

    def close(self):
        self.page.get_by_role("button", name="Batal").click()
```

## Template — Tab

```python
# pages/<module>/components/tabs/<nama>_tab.py

from pages.base_page import BasePage


class <Nama>Tab(BasePage):

    def fill_<something>(self, value: str):
        self.page.get_by_label("<Label>").fill(value)

    def save(self):
        self.page.get_by_role("button", name="Simpan Perubahan").click()
```

## Template — Section

```python
# pages/<module>/components/<nama>_section.py

from pages.base_page import BasePage


class <Nama>Section(BasePage):

    def apply_filter(self, <param>: str):
        self.page.get_by_label("<Filter Label>").select_option(<param>)

    def clear_filter(self):
        self.page.get_by_role("button", name="Reset").click()
```

## Cara Pakai Component di Test

```python
# tests/master_student/test_add_student.py

from pages.master_student.components.add_student_modal import AddStudentModal


def test_add_student(student_page, valid_student_data):
    # Arrange
    modal = AddStudentModal(student_page.page)  # ← passing page dari fixture

    # Act
    student_page.open_add_student_modal()  # ← Page buka modal
    modal.fill_student_form(name=..., email=...)  # ← Component isi form
    modal.submit()

    # Assert
    expect(...).to_be_visible()
```

## Workflow

1. **Tanya user**: component apa (modal/tab/section), field/aksi apa saja di dalamnya.
2. **Pastikan Page Object parent sudah ada** — jika belum, panggil skill `pom` dulu.
3. **Tentukan lokasi**: `pages/<module>/components/` atau `pages/<module>/components/tabs/` untuk tab.
4. **Identifikasi method yang perlu**:
   - Form filling: `fill_<something>()`
   - Aksi submit: `submit()`
   - Close/cancel: `close()`
   - Interaksi lain: dropdown, radio, checkbox, file upload
5. **Generate Component** dengan locator sesuai prioritas (lihat skill `locator`).
6. **Jika locator belum pasti** — minta user codegen/inspect dulu via skill `debug`.
7. **Update Page Object** parent untuk tambah method `open_<component>()` kalau belum ada.

## Anti-Pattern (DILARANG)

```python
# ❌ Assertion di Component
class AddStudentModal(BasePage):
    def submit(self):
        self.page.get_by_role("button", name="Simpan").click()
        expect(self.page.get_by_text("Sukses")).to_be_visible()  # ❌

# ❌ Navigasi di Component
class AddStudentModal(BasePage):
    def open(self):
        self.page.goto("/master-student")  # ❌ ini tugas Page!
        self.page.get_by_role("button", name="Tambah").click()

# ❌ Satu Component multi-modal
class StudentModals(BasePage):  # ❌ pisah jadi AddStudentModal + EditStudentModal
    def fill_add_form(self, ...): ...
    def fill_edit_form(self, ...): ...
```

## Referensi

- Full guideline: [docs/testing-guidelines.md](../../../docs/testing-guidelines.md) section 6, 7
- Page Object parent: skill `pom`
- Locator rules: skill `locator`
