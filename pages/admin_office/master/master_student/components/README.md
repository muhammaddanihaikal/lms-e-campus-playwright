# Master Student Page Objects

Struktur Page Object Model untuk fitur Master Student yang terorganisir per tab.

## Struktur File

```
components/
├── personal_info_tab.py         # Tab Personal Info
├── family_emergency_tab.py      # Tab Family & Emergency
├── education_academic_tab.py    # Tab Education & Academic
├── add_student_modal.py         # Main modal (composer)
├── edit_student_modal.py        # Edit student modal
└── student_detail_modal.py      # Student detail modal
```

## Tab Components

### 1. PersonalInfoTab
Mengelola form informasi pribadi siswa:
- Full Name
- Email
- NISN
- Gender
- Religion
- Date of Birth
- Place of Birth
- Phone Number
- Address

**Usage:**
```python
personal_tab = PersonalInfoTab(page)
personal_tab.fill({
    "full_name": "John Doe",
    "email": "john@example.com",
    "nisn": "1234567890",
    "gender": "Male",
    "religion": "Islam",
    "date_of_birth": "2000-01-01",
    "place_of_birth": "Jakarta",
    "phone": "081234567890",
    "address": "Jl. Example St. 123"
})
```

### 2. FamilyEmergencyTab
Mengelola form informasi keluarga dan kontak darurat:
- Parent Name
- Parent Phone
- Contact Name (Emergency)
- Contact Phone (Emergency)
- Relationship

**Usage:**
```python
family_tab = FamilyEmergencyTab(page)
family_tab.fill({
    "parent_name": "Jane Doe",
    "parent_phone": "081234567890",
    "contact_name": "John Sr.",
    "contact_phone": "081234567891",
    "relationship": "Parent"
})
```

### 3. EducationAcademicTab
Mengelola form pendidikan dan akademik:
- High School
- Graduation Year
- Previous Education Level
- NIM (auto-generated)
- Department
- Semester
- Degree
- Class Type
- Entry Path

**Usage:**
```python
edu_tab = EducationAcademicTab(page)
nim = edu_tab.fill({
    "high_school": "SMAN 1 Jakarta",
    "grad_year": "2024",
    "prev_education": "Senior High School (SMA/SMK)",
    "department": "49",
    "semester": "1",
    "degree": "S1 (Bachelor)",
    "class_type": "Regular",
    "entry_path": "Regular"
})
```

## AddStudentModal

Modal utama yang mengkomposisikan semua tab.

**Usage:**
```python
add_modal = AddStudentModal(page)
nim = add_modal.fill_form(student_data)
add_modal.submit()
```

## Data Structure

Lihat `data/student_data.py` untuk contoh struktur data lengkap yang dibutuhkan.

## Update Locator

Locator diperbarui pada **6 April 2026** berdasarkan codegen dari aplikasi versi terbaru.

### Perubahan Locator:
| Field | Locator Lama | Locator Baru |
|-------|--------------|--------------|
| Email | `Personal Email` | `Email` |
| NISN | `National Student ID (NISN)` | `NISN` |
| Address | `Complete Address` | `Address` |
| Parent Name | `Parent/Guardian Name` | `Parent Name` |
| Parent Phone | `Parent/Guardian Phone` | `Parent Phone` |
| Emergency Contact | `Emergency Contact Name` | `Contact Name` |
| Emergency Phone | `Emergency Contact Phone` | `Contact Phone` |
| High School | `High School Name` | `High School` |
| Graduation Year | `Graduation Year` | `Grad Year*` |
| Education Level | `Previous Education Level` | `Previous Education Level*` |
| Generate Button | `Generate Student ID` | `Gen` |
| Department | `Department` | `Department*` |
| Semester | `Current Semester` | `Semester*` |
| Save Button | `save` | `Save` |
