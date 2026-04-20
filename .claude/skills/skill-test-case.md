---
name: test-case
description: Gunakan skill ini saat user meminta membuat atau menambah test case — baik di file test Python maupun di dokumentasi test case (MD + CSV). Termasuk permintaan seperti "bikin test case untuk login", "tambah test untuk fitur edit profile", "generate test untuk CRUD project", "buatkan regression test", atau saat user ingin menambah coverage (positive, negative, edge case) untuk sebuah fitur.
---

# Generate Test Case

Skill untuk membuat test case baru — mencakup dua hal:
1. **Dokumentasi** — tambah entry ke file `docs/test_cases/<module>.md` dan `docs/test_cases/test_cases.csv`
2. **Implementasi** — tambah test function ke file `tests/<module>/test_<module>.py`

## Struktur Dokumentasi Test Case

### Kolom CSV (`docs/test_cases/test_cases.csv`)

| Kolom | Keterangan |
|-------|-----------|
| `No.` | Nomor urut global (auto-increment dari TC terakhir) |
| `Module` | Nama modul (Authentication, Profile, Project, dst) |
| `Sub Menu` | Sub-menu atau halaman spesifik (Login, Tab Profile, dst) |
| `TC ID` | ID unik global: `TC-<nomor>` |
| `Test Case Title` | Judul test case (tanpa emoji status) |
| `Description` | Tipe skenario: Positive case / Negative case / Edge case |
| `Precondition` | Kondisi awal sebelum test dijalankan (misal: User sudah login) |
| `Priority` | High / Normal |
| `Steps` | Langkah-langkah test (numbered list) |
| `Expected Results` | Hasil yang diharapkan (numbered list) |
| `Status` | Passed / Pending / Skipped / Blocked / Unknown |

### Format File MD (`docs/test_cases/<module>.md`)

```markdown
### TC-<id>: <status-emoji> <STATUS> — <Judul Test Case>

- **Sub Menu**: <sub-menu>
- **Priority**: <🔴 High | 🟡 Normal>
- **Description**: <Positive case | Negative case | Edge case>
- **Precondition**: <kondisi awal, misal: 1. User sudah login ke sistem>
- **Test Status**: <status teks>

**Steps:**
   1. <langkah 1>
   2. <langkah 2>

**Expected Results:**
   - 1. <hasil yang diharapkan dari langkah 1>
   - 2. <hasil yang diharapkan dari langkah 2>

---
```

**Status emoji:**
- `🟢 PASSED` — test sudah jalan & passed
- `🟡 PENDING` — test ada tapi belum sempurna
- `❌ BLOCKED` — gagal karena kendala eksternal
- `⏭️ SKIPPED` — sengaja di-skip
- `🟡 UNKNOWN` — belum dijalankan, status belum diketahui

## Struktur Implementasi Test (Python)

```python
@allure.title("TC-<id>: <status-emoji> <STATUS> — <Judul>")
def test_<snake_case_judul>(login_as_tester):
    # Arrange
    page = login_as_tester
    <page_object> = <PageClass>(page)

    # Act
    <aksi user>

    # Assert
    expect(<elemen>).<matcher>()
```

## Aturan WAJIB

1. **TC ID global** — lanjut dari TC terakhir di seluruh project:
   ```bash
   grep -rh "@allure.title" tests/ | grep -oE "TC-[0-9]+" | sort -V | tail -1
   ```
2. **Wajib update dua tempat**: file MD di `docs/test_cases/` + CSV `test_cases.csv` + file test Python di `tests/`
3. **Status emoji awal** = `🟡 PENDING` sebelum dijalankan
4. **No `time.sleep()`** — pakai `expect()` atau `wait_for_*`
5. **No assertion di POM** — assertion hanya di test function
6. **Test isolation** — setiap test independen, tidak bergantung test lain

## Coverage Wajib per Fitur

| Tipe | Deskripsi | Contoh |
|------|-----------|--------|
| ✅ Positive case | Input valid → berhasil | Login dengan data valid |
| ❌ Negative case | Input invalid → muncul error | Login dengan email salah |
| 🔲 Edge case | Kondisi batas / khusus | Field kosong, karakter spesial |

## Contoh Lengkap — Positive Case

**Dokumentasi MD:**
```markdown
### TC-18: 🟡 PENDING — Membuka halaman Dashboard

- **Sub Menu**: Dashboard
- **Priority**: 🔴 High
- **Description**: Positive case
- **Precondition**: 1. User sudah login ke sistem

**Steps:**
   1. Klik menu Dashboard

**Expected Results:**
   - 1. Menampilkan halaman dashboard dengan data yang sesuai

---
```

**CSV row:**
```
18, Dashboard, Dashboard, TC-18, Membuka halaman Dashboard, Positive case, 1. User sudah login ke sistem, High, "1. Klik menu Dashboard", "1. Menampilkan halaman dashboard dengan data yang sesuai", Pending
```

**Implementasi Python:**
```python
@allure.title("TC-18: 🟡 PENDING — Membuka halaman Dashboard")
def test_open_dashboard(login_as_tester):
    # Arrange
    page = login_as_tester
    dashboard = DashboardPage(page)

    # Act
    dashboard.navigate()

    # Assert
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
```

## Contoh — Negative Case

**Dokumentasi MD:**
```markdown
### TC-19: 🟡 PENDING — Login dengan password kosong

- **Sub Menu**: Login
- **Priority**: 🔴 High
- **Description**: Negative case
- **Precondition**: 1. User berada di halaman login

**Steps:**
   1. Input email yang valid
   2. Kosongkan field password
   3. Klik button Login

**Expected Results:**
   - 1. Berhasil menginput email
   - 2. Field password kosong
   - 3. Menampilkan alert 'password is required'

---
```

## Contoh — Skipped

```python
@allure.title("TC-20: ⏭️ SKIPPED — Upload foto profile")
@pytest.mark.skip(reason="File input dialog butuh strategi fixture khusus")
def test_upload_profile_photo(login_as_tester):
    ...
```

## Contoh — Regression Test

```markdown
### TC-REG-1: 🟡 PENDING — Regression: Button login tidak disabled setelah submit gagal

- **Sub Menu**: Login
- **Priority**: 🔴 High
- **Description**: Regression case
- **Precondition**: 1. User berada di halaman login

**Steps:**
   1. Input credential salah
   2. Klik button Login
   3. Tunggu response error

**Expected Results:**
   - 1. Button Login kembali enabled setelah response error

---
```

## Workflow

1. **Tanya user**: fitur apa, skenario apa (positive/negative/edge), sub menu mana
2. **Cari TC ID terakhir**:
   ```bash
   grep -rh "@allure.title" tests/ | grep -oE "TC-[0-9]+" | sort -V | tail -1
   ```
3. **Cek prasyarat**: Page Object & fixture sudah ada? → skill `pom`, `fixture`
4. **Generate dokumentasi** — tambah entry di `docs/test_cases/<module>.md`
5. **Update CSV** — tambah row baru di `docs/test_cases/test_cases.csv`
6. **Generate implementasi** — tambah test function di `tests/<module>/test_<module>.py`
7. **Run test**:
   ```bash
   # Run + buka report (pakai skill test-report)
   pytest tests/<module>/test_<module>.py -v --alluredir=allure-results && allure serve allure-results
   ```
8. **Update status emoji** di MD, CSV, dan `@allure.title` sesuai hasil run

## File Referensi

- Dokumentasi: `docs/test_cases/<module>.md`
- Semua TC (CSV): `docs/test_cases/test_cases.csv`
- Implementasi: `tests/<module>/test_<module>.py`

## Referensi Skill

- Buat FILE test baru: skill `test`
- Page Object: skill `pom` | Component: skill `component`
- Fixture: skill `fixture` | Locator: skill `locator`
- Run + report: skill `test-report`
