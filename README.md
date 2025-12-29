# LMS E-Campus Automation with Playwright Python

Proyek otomasi pengujian untuk sistem LMS E-Campus menggunakan Python dan Playwright dengan pola desain **Page Object Model (POM)**.

## 🚀 Fitur Utama
- **Login:** Automasi login berbagai role.
- **Master Student:** Tambah, Lihat Detail, dan Hapus data mahasiswa.
- **E2E Testing:** Student Lifecycle (Tambah -> Verifikasi Detail -> Hapus).

## 🛠️ Persiapan
1. **Buat Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   ```
2. **Install Library:**
   ```bash
   pip install playwright pytest
   playwright install chromium
   ```

## 🧪 Cara Menjalankan Test
- **Jalankan Semua Test:**
  ```bash
  pytest
  ```
- **Jalankan Test Spesifik:**
  ```bash
  pytest test/test_add_student.py
  ```
- **Jalankan E2E Test:**
  ```bash
  pytest test/e2e/test_student_lifecycle.py
  ```

## 📂 Struktur Proyek
- `pages/`: Berisi class Page Object (Locator & Fungsi).
- `test/`: Berisi skrip pengujian (Pytest).
- `data/`: Data uji (Input form, kredensial).
- `config/`: Konfigurasi dasar (URL, dsb).
