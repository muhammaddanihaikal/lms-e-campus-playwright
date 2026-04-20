---
name: debug
description: Gunakan skill ini saat user ingin debug locator yang gagal, explore elemen baru di UI, atau record flow interaksi. Termasuk permintaan seperti "locator ini gagal, gimana cara cari yang benar?", "aku mau codegen halaman X", "bantu cari locator tombol Y", "trace file gagal test". Skill ini mengarahkan penggunaan Playwright CLI (Inspector, Codegen, Trace Viewer) — TIDAK generate code langsung, tapi arahkan user pakai tool interaktif.
---

# Debug Locator — Playwright CLI

Skill untuk debug, explore, dan record locator pakai Playwright CLI tools.

## Setup (cek dulu)

```bash
# Cek apakah Playwright CLI sudah terinstall
playwright --version

# Kalau belum, install global
npm install -g @playwright/test
```

## Tiga Tools Utama

### 1. Playwright Inspector (explore interaktif)

```bash
playwright inspect <URL>
```

**Kapan pakai:**
- Mau lihat opsi locator untuk satu elemen
- Test selector live sebelum masukkan ke code
- Cek accessibility role, label, text dari elemen
- Debug locator yang gagal di test

**Cara kerja:**
1. Buka URL di browser Playwright
2. Hover elemen → lihat semua opsi locator
3. Pilih locator sesuai prioritas (role > label > placeholder > text > testid > CSS)
4. Copy ke page object

### 2. Playwright Codegen (record flow)

```bash
playwright codegen <URL>
```

**Kapan pakai:**
- Record flow kompleks (multi-step user journey)
- Explore page yang masih asing
- Generate baseline code yang nanti di-refactor ke POM

**Cara kerja:**
1. Interact dengan UI seperti user normal
2. Playwright generate code otomatis
3. Copy code → **WAJIB refactor** ke pattern POM dengan locator priority
4. Jangan langsung paste ke production code

### 3. Trace Viewer (debug test gagal)

```bash
playwright show-trace <path/to/trace.zip>
```

**Kapan pakai:**
- Test gagal di CI dan susah direproduksi lokal
- Mau lihat network requests + DOM snapshot saat gagal

**Setup trace recording di fixture:**

```python
# conftest.py
context = browser.new_context(record_trace_dir="traces/")
```

## Workflow 1 — Locator Gagal di Test

```
Step 1: Test gagal
  pytest tests/authentication/test_authentication.py::test_login -v
  # FAILED: page.get_by_role("button", name="Login") not found

Step 2: Buka Inspector
  playwright inspect http://localhost:3000/login

Step 3: Hover button Login → lihat opsi locator
  # Opsi 1: page.get_by_role("button", name="login")  # case-sensitive
  # Opsi 2: page.get_by_text("Login")
  # Opsi 3: page.locator("button:has-text('Login')")

Step 4: Pilih yang sesuai prioritas + validasi di Inspector
  # page.get_by_role("button", name="Login", exact=True)

Step 5: Update page object
  # pages/login_page.py:
  #   self.page.get_by_role("button", name="Login", exact=True).click()

Step 6: Re-run test
  pytest tests/authentication/test_authentication.py::test_login -v
  # PASSED ✅
```

## Workflow 2 — Record Flow Baru & Generate POM

```
Step 1: Mulai codegen
  playwright codegen http://localhost:3000/login

Step 2: Interact dengan UI
  - Fill email
  - Fill password
  - Click login
  - Tunggu dashboard load

Step 3: Playwright generate code, misal:
  page.fill('input[name="email"]', "admin@test.com")
  page.fill('input[name="password"]', "secret")
  page.locator('button[type="submit"]').click()

Step 4: Refactor ke POM dengan locator priority
  # pages/login_page.py
  class LoginPage(BasePage):
      def login(self, email, password):
          self.page.get_by_label("Email").fill(email)             # Priority 2
          self.page.get_by_label("Password").fill(password)       # Priority 2
          self.page.get_by_role("button", name="Login").click()   # Priority 1

Step 5: Validasi refactored locator di Inspector
  playwright inspect http://localhost:3000/login
  # hover setiap elemen → confirm role/label match
```

## Pakai dengan BASE_URL dari .env

```bash
# Unix / Git Bash
BASE_URL=$(grep BASE_URL .env | cut -d= -f2)
playwright inspect "$BASE_URL/login"
playwright codegen "$BASE_URL/login"
```

## Before / After — Refactor Hasil Codegen

**Before (hasil codegen mentah, fragile):**
```python
# ❌ Hardcoded CSS, mudah break
self.page.locator(".profile-form input[type='text']").fill(new_name)
```

**Setelah inspect elemen:**
- Role: `textbox`
- Label: `"Full Name"`
- Placeholder: `"Enter your full name"`

**After (robust, ikut priority):**
```python
# ✅ Priority #2 (Label), validasi di Inspector
self.page.get_by_label("Full Name").fill(new_name)
```

## Best Practices

| Do ✅ | Don't ❌ |
|-------|----------|
| Pakai Inspector untuk explore elemen baru | Hardcode locator tanpa test dulu |
| Pakai Codegen untuk record flow kompleks | Copy-paste hasil codegen ke production langsung |
| Ikut priority (role → label → placeholder → text → testid → CSS) | Pakai XPath/CSS kompleks dari codegen |
| Test locator di Inspector sebelum update POM | Update locator tanpa validasi manual |
| Refactor generated code ke pattern POM | Tinggalkan generated code apa adanya |

## Troubleshooting

| Masalah | Solusi |
|---------|--------|
| Inspector tidak bisa terhubung ke app | Pastikan app running, URL correct, tidak perlu auth |
| Locator dari Codegen tidak jalan saat test | Test dulu di Inspector, refactor ke priority strategy |
| Elemen modal tidak bisa di-hover | Inspector support modal — pastikan modal sudah open |
| App butuh login dulu | Login manual di Inspector window, baru hover target |
| Lambat / stuck | Coba `--browser=chromium` atau close tab lain |

## Workflow untuk AI

1. **Tanya user**: apa masalahnya (locator gagal / explore page baru / debug trace).
2. **Kalau locator gagal di test existing:**
   - Lihat test file → identifikasi locator bermasalah
   - Arahkan user jalankan `playwright inspect <URL>`
   - Tunggu user lapor opsi locator yang muncul di Inspector
   - Propose locator baru sesuai prioritas — **jangan auto apply**
3. **Kalau explore page baru / record flow:**
   - Arahkan user jalankan `playwright codegen <URL>`
   - Minta user paste hasil codegen
   - Refactor ke pattern POM dengan locator priority
4. **Kalau debug trace:**
   - Arahkan user jalankan `playwright show-trace <trace-file>`
   - Tanya apa yang dilihat di timeline / network / DOM snapshot
5. **Jangan auto-fix** — selalu propose perubahan dan tunggu konfirmasi user.

## Referensi

- Full guideline: [docs/testing-guidelines.md](../../../docs/testing-guidelines.md) section 18
- CLAUDE.md section "Playwright CLI for Locator Debugging"
- Locator priority: skill `locator`
