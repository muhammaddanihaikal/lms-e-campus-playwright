---
name: locator
description: Gunakan skill ini saat user bertanya atau meminta bantuan soal locator Playwright — memilih locator terbaik, mengubah locator fragile jadi robust, atau mereview locator di page object. Termasuk permintaan seperti "locator yang benar untuk button X apa?", "ganti CSS selector ini ke role", "review locator di file ini", "kenapa locator ini gagal?". WAJIB dipakai sebagai referensi saat skill lain (generate-page-object, generate-component) menulis locator.
---

# Locator Strategy

Skill referensi untuk memilih dan menulis locator Playwright mengikuti standar project ini.

## Prioritas Locator (WAJIB diikuti urut)

### ✅ Prioritas 1 — Role (PALING DIUTAMAKAN)

```python
page.get_by_role("button", name="Login")
page.get_by_role("textbox", name="Email")
page.get_by_role("link", name="Lupa password")
page.get_by_role("tab", name="Informasi Pribadi")
page.get_by_role("row", name="Budi Santoso")
page.get_by_role("option", name="Kelas 10A")
page.get_by_role("heading", name="Dashboard")
page.get_by_role("dialog", name="Tambah Siswa")
```

**Kapan pakai:** hampir selalu. Ini yang paling robust karena ikut accessibility tree.

### ✅ Prioritas 2 — Label

```python
page.get_by_label("Email")
page.get_by_label("Password")
page.get_by_label("Tanggal Lahir")
```

**Kapan pakai:** untuk form field yang punya `<label>` terhubung.

### ✅ Prioritas 3 — Placeholder

```python
page.get_by_placeholder("Masukkan email")
page.get_by_placeholder("cari siswa...")
```

**Kapan pakai:** form tanpa label eksplisit tapi punya placeholder.

### ✅ Prioritas 4 — Text (untuk elemen statis)

```python
page.get_by_text("Selamat datang")
page.get_by_text("Data berhasil disimpan")
```

**Kapan pakai:** heading/label statis, pesan notifikasi. **HATI-HATI:** jangan pakai untuk text yang sering berubah (tanggal, angka dinamis).

### ✅ Prioritas 5 — data-testid

```python
page.get_by_test_id("login-button")
page.get_by_test_id("student-table-row")
```

**Kapan pakai:** jika developer sudah menyediakan. **Sarankan ke developer** untuk menambahkan `data-testid` pada elemen penting jika tidak ada pilihan role/label yang bagus.

### ⚠️ Prioritas 6 — CSS Selector (last resort)

```python
page.locator("button[type='submit']")
page.locator("input[name='email']")
```

**Kapan pakai:** HANYA jika role/label/testid semuanya tidak bisa.

### ❌ Prioritas 7 — XPath (HINDARI)

```python
page.locator("//button[@type='submit']")  # ❌ jangan
```

**Kapan pakai:** Hampir tidak pernah. Jika ada opsi lain, WAJIB pakai yang lain.

## Anti-Pattern (DILARANG)

```python
# ❌ Posisi-based
page.locator("div > div > div > button")

# ❌ nth-child
page.locator("li:nth-child(3)")

# ❌ Class dinamis / generated (misal dari Tailwind JIT / CSS-in-JS)
page.locator(".btn-a1b2c3")
page.locator("._1xKz2Y")

# ❌ Text yang sering berubah
page.get_by_text("12 April 2025")
page.get_by_text("Saldo: Rp 1.500.000")

# ❌ Kombinasi CSS panjang dan fragile
page.locator("form.auth > div.field:nth-child(2) > input")
```

## Locator Chaining (Scoping)

Untuk elemen dalam container (row, modal, section), pakai chaining:

```python
# Row dengan button Edit
row = page.get_by_role("row", name="Budi Santoso")
row.get_by_role("button", name="Edit").click()

# Dialog dengan field di dalamnya
dialog = page.get_by_role("dialog", name="Tambah Siswa")
dialog.get_by_label("Nama").fill("Budi")
dialog.get_by_role("button", name="Simpan").click()

# Section tertentu
section = page.get_by_role("region", name="Filter")
section.get_by_label("Status").select_option("Aktif")
```

## Common Use Cases

### Button

```python
page.get_by_role("button", name="Login")
page.get_by_role("button", name="Tambah Siswa")
```

### Input / TextBox

```python
page.get_by_label("Email")           # Prioritas 2
page.get_by_role("textbox", name="Email")  # Prioritas 1
page.get_by_placeholder("Masukkan email")  # Prioritas 3
```

### Dropdown / Select

```python
# Native <select>
page.get_by_label("Status").select_option("Aktif")

# Custom dropdown (combobox)
page.get_by_role("combobox", name="Kelas").click()
page.get_by_role("option", name="10A").click()
```

### Checkbox / Radio

```python
page.get_by_role("checkbox", name="Setuju dengan syarat").check()
page.get_by_role("radio", name="Laki-laki").check()
```

### Link

```python
page.get_by_role("link", name="Lupa password")
```

### Table Row

```python
row = page.get_by_role("row", name="Budi Santoso")
row.get_by_role("button", name="Edit").click()
```

### Modal / Dialog

```python
dialog = page.get_by_role("dialog", name="Konfirmasi Hapus")
dialog.get_by_role("button", name="Hapus").click()
```

### Tab

```python
page.get_by_role("tab", name="Informasi Pribadi").click()
```

### Toast / Notification

```python
expect(page.get_by_role("alert")).to_contain_text("berhasil disimpan")
```

## Handling `exact=True`

Kalau ada beberapa teks mirip (misal "Login" dan "Login Admin"), pakai `exact=True`:

```python
page.get_by_text("Login", exact=True)
page.get_by_role("button", name="Save", exact=True)
```

## Saat Locator Gagal (AI Behavior)

Kalau locator gagal, AI **WAJIB**:
1. **Cari ulang** berdasarkan `role`, `label`, atau `visible text`.
2. **Jangan langsung ganti** tanpa validasi.
3. **Propose perubahan** ke user — jangan auto apply.
4. **Pastikan locator baru** tetap ikut prioritas di atas.
5. **Sarankan pakai skill `debug`** untuk codegen/inspect dulu.

## Refactor Checklist

Saat review locator di file existing, cek:
- [ ] Apakah pakai `role`/`label` atau masih CSS/XPath?
- [ ] Apakah ada class dinamis (mengandung hash random)?
- [ ] Apakah ada `nth-child` atau pattern posisi?
- [ ] Apakah text yang dipakai statis atau bisa berubah?
- [ ] Bisakah di-scope dengan chaining (row/dialog) untuk lebih robust?

## Referensi

- Full guideline: [docs/testing-guidelines.md](../../../docs/testing-guidelines.md) section 4
- Untuk menemukan locator yang tepat di UI: skill `debug`
