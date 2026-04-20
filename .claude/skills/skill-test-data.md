---
name: test-data
description: Gunakan skill ini saat user meminta membuat test data — file JSON valid/invalid, helper faker untuk data dinamis, atau data dummy per module. Termasuk permintaan seperti "bikin test data siswa valid", "generate invalid login data", "buat faker helper untuk user random", "tambah data dummy untuk edge case".
---

# Generate Test Data

Skill untuk membuat test data — JSON files atau Faker helper — mengikuti standar project ini.

## Dua Jenis Test Data

### 1. Static JSON (data tetap, dipanggil via fixture)

Taruh di `data/<module>/<scenario>_<entity>.json`.

**Kapan pakai:**
- Data yang sama dipakai berkali-kali
- Data negative case dengan nilai spesifik (misal email `"bukan-email"`)
- Data reference (misal daftar kelas valid)

### 2. Dynamic Faker (generate tiap test)

Taruh helper di `utils/faker_helper.py`.

**Kapan pakai:**
- Data harus unique tiap test (email unique, nomor HP unique)
- Smoke test dengan nilai apa saja
- Volume test

## Struktur Folder

```
data/
├── <module>/
│   ├── valid_<entity>.json          # Positive case
│   ├── invalid_<entity>.json        # Negative case
│   └── edge_<entity>.json           # Edge case

utils/
├── faker_helper.py                  # Dynamic data generator
└── date_helper.py                   # Helper tanggal, format, dll
```

## Template — Valid Data (Positive Case)

```json
// data/master_student/valid_student.json
{
  "name": "Budi Santoso",
  "email": "budi.santoso@example.com",
  "phone": "08123456789",
  "birth_date": "2005-08-17",
  "class": "10A"
}
```

## Template — Invalid Data (Negative Case)

```json
// data/master_student/invalid_student.json
{
  "name": "",
  "email": "bukan-email",
  "phone": "abc",
  "birth_date": "tanggal-invalid"
}
```

## Template — Edge Case Data

```json
// data/master_student/edge_student.json
{
  "name_too_long": "Budi Santoso Iskandar Muda Al-Rasyid Bin Abdullah Al-Haitam Ibnu Sina",
  "name_special_char": "Budi @#$%^&",
  "email_unicode": "bùdì@example.com",
  "phone_international": "+628123456789"
}
```

## Template — Faker Helper

```python
# utils/faker_helper.py

from faker import Faker

fake = Faker("id_ID")  # Locale Indonesia


def generate_student():
    """Generate random student data"""
    return {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "birth_date": fake.date_of_birth(minimum_age=10, maximum_age=18).isoformat(),
    }


def generate_admin():
    """Generate random admin user"""
    return {
        "name": fake.name(),
        "email": fake.company_email(),
        "password": fake.password(length=12),
    }


def generate_project():
    """Generate random project data"""
    return {
        "name": fake.catch_phrase(),
        "description": fake.text(max_nb_chars=200),
        "start_date": fake.date_this_year().isoformat(),
        "end_date": fake.date_between(start_date="+1m", end_date="+6m").isoformat(),
    }
```

## Cara Pakai — Static JSON

**1. Bikin fixture di `tests/<module>/conftest.py`** (lihat skill `fixture`):

```python
import pytest
import json


@pytest.fixture
def valid_student_data():
    with open("data/master_student/valid_student.json") as f:
        return json.load(f)
```

**2. Pakai di test:**

```python
def test_add_student(student_page, valid_student_data):
    # Arrange
    modal = AddStudentModal(student_page.page)

    # Act
    student_page.open_add_student_modal()
    modal.fill_student_form(
        name=valid_student_data["name"],
        email=valid_student_data["email"]
    )
    modal.submit()

    # Assert
    expect(student_page.page.get_by_text(valid_student_data["name"])).to_be_visible()
```

## Cara Pakai — Faker Helper

**1. Bikin fixture di `tests/<module>/conftest.py`:**

```python
import pytest
from utils.faker_helper import generate_student


@pytest.fixture
def random_student_data():
    return generate_student()
```

**2. Pakai di test:**

```python
def test_add_student_with_random_data(student_page, random_student_data):
    # Arrange
    modal = AddStudentModal(student_page.page)

    # Act
    student_page.open_add_student_modal()
    modal.fill_student_form(
        name=random_student_data["name"],
        email=random_student_data["email"]
    )
    modal.submit()

    # Assert
    expect(student_page.page.get_by_text(random_student_data["name"])).to_be_visible()
```

## Pattern — Kombinasi Static + Dynamic

Kalau butuh base data tapi beberapa field harus unique:

```python
# utils/faker_helper.py
def with_unique_email(base_data):
    import copy
    data = copy.deepcopy(base_data)
    data["email"] = fake.email()
    return data
```

```python
# Test
def test_create_student(student_page, valid_student_data):
    data = with_unique_email(valid_student_data)  # email unique tiap run
    ...
```

## Aturan WAJIB

1. **Lokasi**: data statis WAJIB di `data/<module>/`, bukan dalam test file.
2. **Naming JSON**: `<scenario>_<entity>.json` (contoh: `valid_student.json`, `invalid_project.json`).
3. **Struktur data**: konsisten (field yang sama antar file valid/invalid supaya gampang di-swap).
4. **JANGAN** hardcode data sensitif (password admin, API key) — itu di `.env`.
5. **Faker locale**: pakai `"id_ID"` untuk data Indonesia (nama, nomor HP, alamat).
6. **JANGAN** commit data yang berisi info sensitif/PII real.

## Workflow

1. **Tanya user**: data untuk module apa, skenario apa (valid/invalid/edge), field apa saja.
2. **Tentukan tipe data**:
   - Perlu unique tiap run? → Faker helper
   - Nilai harus spesifik (misal negative case)? → Static JSON
3. **Bikin file** di lokasi yang benar.
4. **Update `tests/<module>/conftest.py`** tambah fixture yang load data (panggil skill `fixture` kalau perlu).
5. **Konfirmasi struktur data** dengan user — field apa saja yang dibutuhkan test.

## Anti-Pattern (DILARANG)

```python
# ❌ Hardcode data di test
def test_add_student(student_page):
    modal.fill_student_form(name="Budi", email="budi@test.com")  # ❌

# ❌ Data sensitif di JSON committed
# data/admin/credentials.json
{ "password": "rahasia123" }  # ❌ taruh di .env!

# ❌ Struktur tidak konsisten
# valid_student.json: { "name": ..., "email": ... }
# invalid_student.json: { "nama": ..., "mail": ... }  # ❌ field berbeda, susah swap
```

## Referensi

- Full guideline: [docs/testing-guidelines.md](../../../docs/testing-guidelines.md) section 6 (Data & Utils)
- Fixture: skill `fixture`
- Test case: skill `test-case`
