---
name: test-report
description: Gunakan skill ini saat user ingin menjalankan tests DAN langsung membuka Allure report di browser — satu langkah, selesai. Termasuk permintaan seperti "run test terus buka report", "jalankan semua test dan lihat hasilnya", "run authentication tests dan generate report", "execute tests dan show allure". Ini kombinasi dari pytest + allure serve.
---

# Test & Report

Skill untuk menjalankan **tests + Allure report** dalam satu flow.

## Workflow Otomatis

```
1. pytest tests/ --alluredir=allure-results
2. allure serve allure-results
```

Hasil:
- Test dijalankan dengan pytest
- Report di-generate di folder `allure-results/`
- Browser otomatis buka Allure dashboard (localhost:8080)

## Opsi Run

### Semua test di project

```bash
pytest tests --alluredir=allure-results && allure serve allure-results
```

**Kapan pakai**: smoke test project, check overall health.

### Test spesifik module

```bash
pytest tests/<module> -v --alluredir=allure-results && allure serve allure-results
```

**Contoh:**
```bash
pytest tests/authentication -v --alluredir=allure-results && allure serve allure-results
pytest tests/profile -v --alluredir=allure-results && allure serve allure-results
pytest tests/project -v --alluredir=allure-results && allure serve allure-results
```

### Test file tunggal

```bash
pytest tests/<module>/test_<module>.py -v --alluredir=allure-results && allure serve allure-results
```

**Contoh:**
```bash
pytest tests/authentication/test_authentication.py::test_login_valid_credentials -v --alluredir=allure-results && allure serve allure-results
```

## Workflow — Kapan Pakai Skill Ini

1. **Setelah implementasi test baru** — run + lihat langsung hasilnya di Allure
2. **Debug test yang gagal** — run test yang specific + lihat error di Allure dashboard
3. **Verify coverage** — run semua test, check Allure untuk lihat TC mana yang passing/failing/skipped
4. **Sebelum commit** — pastikan semua test lolos sebelum push

## Allure Report Features

Dashboard Allure menampilkan:
- **Test summary** — total, passed, failed, skipped
- **Status timeline** — durasi test, trend
- **Test details** — error message, screenshot on failure
- **Categories** — group test by suite/module
- **Graphs** — visualization status distribution

## Command Variations

### Run dengan verbose output

```bash
pytest tests/ -v --alluredir=allure-results && allure serve allure-results
```

### Run hanya test tertentu (filtering)

```bash
# Hanya test yang sudah PASSED
pytest tests/ -m "not skipped" --alluredir=allure-results && allure serve allure-results

# Hanya test tertentu saja (misal "login")
pytest tests/ -k "login" -v --alluredir=allure-results && allure serve allure-results
```

### Run dengan failure stop (henti saat ada gagal)

```bash
pytest tests/ -x --alluredir=allure-results && allure serve allure-results
```

## Prasyarat

Pastikan terinstall:
```bash
pip install pytest allure-pytest
npm install -g allure-commandline
playwright install
```

Atau sudah ter-install via `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Tips

1. **Browser tidak buka otomatis?** → Open `localhost:8080` manual di browser (atau cek port berbeda jika sudah dipakai).
2. **Report kosong?** → Pastikan test punya `@allure.title()` decorator. Lihat skill `test` atau `test-case`.
3. **Mau clear report lama** → Hapus folder `allure-results/` sebelum run: `rm -rf allure-results/`
4. **Screenshot tidak muncul?** → Pastikan hook di `conftest.py` root sudah ada untuk capture on failure.

## Workflow Manual (tanpa skill ini)

Kalau user prefer jalankan per-step:

```bash
# Step 1: Run test
pytest tests/ --alluredir=allure-results

# Step 2: Generate & open report (terpisah)
allure serve allure-results
```

Tapi lebih praktis gunakan skill ini untuk one-liner.

## Referensi

- docs/testing-guidelines.md section 15 (CI/CD)
- Allure official: https://docs.qameta.io/allure/
- Skill test saja: skill `test`
