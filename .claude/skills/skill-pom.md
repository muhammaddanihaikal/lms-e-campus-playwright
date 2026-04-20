---
name: pom
description: Gunakan skill ini saat user meminta membuat Page Object baru untuk sebuah halaman (bukan komponen/modal). Termasuk permintaan seperti "bikin page object untuk halaman settings", "generate POM untuk halaman report", "tambah page baru". Page Object adalah entry point per halaman — berisi navigasi dan pembuka komponen, TIDAK berisi aksi detail.
---

# Generate Page Object

Skill untuk membuat **Page Object** baru mengikuti pattern POM project ini.

## Konsep Hierarki

```
BasePage (base class)
  └── Page (entry point per halaman)  ← SKILL INI
        └── Component (modal, tab, section)  ← pakai skill `component`
              └── Aksi detail (fill, click, dll)
```

## Aturan WAJIB

1. **Wajib extend `BasePage`** — jangan buat `__init__` sendiri, pakai yang dari BasePage.
2. **Page hanya untuk navigasi & membuka komponen**:
   - `navigate()` — goto halaman
   - `open_<nama>_modal()` — buka modal tertentu
   - `open_<nama>_tab()` — buka tab tertentu
3. **JANGAN** taruh aksi detail (fill form, dsb) di Page — itu tugas Component.
4. **JANGAN** ada assertion di Page Object — assertion hanya di test function.
5. **Naming:**
   - File: `<nama_halaman>_page.py` (snake_case)
   - Class: `<NamaHalaman>Page` (PascalCase)
   - Method: snake_case, deskriptif (`open_add_student_modal`, bukan `openModal1`)
6. **Locator** harus ikut prioritas (lihat skill `locator`).

## Struktur Folder

```
pages/
├── base_page.py
├── <nama_module>/
│   ├── <nama_module>_page.py        ← file yang dibuat skill ini
│   └── components/                   ← diisi via skill `component`
│       ├── <nama_modal>_modal.py
│       └── tabs/
│           └── <nama>_tab.py
```

Untuk halaman tunggal tanpa sub-folder module, boleh langsung di `pages/`:
```
pages/
├── login_page.py
├── dashboard_page.py
```

## Template — Page Object Sederhana

```python
# pages/<module>/<module>_page.py

from pages.base_page import BasePage


class <NamaModule>Page(BasePage):

    def navigate(self):
        self.page.goto("/<route>")
```

## Template — Page dengan Modal & Tab

```python
# pages/master_student/master_student_page.py

from pages.base_page import BasePage


class MasterStudentPage(BasePage):

    def navigate(self):
        self.page.goto("/master-student")

    def open_add_student_modal(self):
        self.page.get_by_role("button", name="Tambah Siswa").click()

    def open_edit_student_modal(self, student_name: str):
        row = self.page.get_by_role("row", name=student_name)
        row.get_by_role("button", name="Edit").click()

    def open_personal_info_tab(self):
        self.page.get_by_role("tab", name="Informasi Pribadi").click()
```

## BasePage (referensi — jangan diubah kecuali perlu helper global)

```python
# pages/base_page.py

class BasePage:
    def __init__(self, page):
        self.page = page
```

Tambah method helper ke BasePage HANYA jika dipakai di banyak page (misal `wait_for_toast()`, `close_any_dialog()`).

## Workflow

1. **Tanya user**: halaman apa yang mau dibuat, route-nya apa, komponen apa saja yang perlu dibuka.
2. **Tentukan lokasi file**: apakah masuk folder module baru atau langsung di `pages/`.
3. **Cek route** — konfirmasi dengan user path URL (misal `/master-student`).
4. **Generate Page Object** dengan navigate + method pembuka komponen.
5. **Untuk locator nama button/row/tab** — pakai teks yang muncul di UI. Jika belum tahu persis, minta user untuk codegen/inspect dulu (panggil skill `debug`).
6. **Setelah Page dibuat**, tawarkan generate Component untuk modal/tab yang disebut (skill `component`).

## Anti-Pattern (DILARANG)

```python
# ❌ Aksi detail di Page
class MasterStudentPage(BasePage):
    def add_student(self, name, email):  # ← ini tugas Component!
        self.page.get_by_role("button", name="Tambah").click()
        self.page.get_by_label("Nama").fill(name)
        ...

# ❌ Assertion di Page
class MasterStudentPage(BasePage):
    def navigate(self):
        self.page.goto("/master-student")
        assert self.page.url == "/master-student"  # ❌ no assert!
```

## Referensi

- Full guideline: [docs/testing-guidelines.md](../../../docs/testing-guidelines.md) section 6, 7
- Component: skill `component`
- Locator rules: skill `locator`
