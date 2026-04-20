---
name: github
description: Panduan commit & push ke GitHub — gunakan bahasa Indonesia, deskripsi singkat
type: reference
---

# Commit & Push ke GitHub

## Standar Commit Message

**Format:** `<type>: <deskripsi singkat dalam bahasa Indonesia>`

### Type yang umum:
- `feat:` — fitur baru / test case baru
- `fix:` — bug fix / perbaikan
- `refactor:` — refactor code
- `docs:` — update dokumentasi
- `test:` — tambah/update test

### Contoh Commit Message:

✅ **BENAR:**
```
feat: implement TC-5 forgot password test
fix: perbaiki locator di LoginPage
docs: update test case documentation
test: add negative case untuk login
refactor: simplify email helper function
```

❌ **SALAH:**
```
update code
fix stuff
TC-5 forgot password
implemented feature with some updates and fixes
```

## Cara Commit & Push

```bash
# 1. Check status
git status

# 2. Stage files
git add docs/test_cases/test_cases.csv pages/login_page.py tests/authentication/test_authentication.py

# 3. Commit dengan pesan singkat (Bahasa Indonesia)
git commit -m "feat: implement TC-5 forgot password test"

# 4. Push ke master
git push origin master
```

## Tips

- **Singkat** — satu baris, max ~50 karakter untuk summary
- **Jelas** — siapa baca, langsung paham apa yang berubah
- **Bahasa Indonesia** — supaya konsisten dalam project ini
- **Imperative mood** — "implement" bukan "implemented", "fix" bukan "fixed"

## Referensi

- Dokumentasi: `docs/test_cases/`
- CSV: `docs/test_cases/test_cases.csv`
- Implementasi: `tests/<module>/test_<module>.py`
