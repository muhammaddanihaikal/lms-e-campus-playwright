# Test Cases — Authentication

### TC-1: 🟡 PENDING — Login sebagai admin office dengan kredensial valid

- **Sub Menu**: Login
- **Priority**: 🔴 High
- **Description**: Positive case
- **Precondition**: 1. Berada di halaman login

**Steps:**
   1. Buka /login
   2. Isi username & password admin office
   3. Klik tombol Login

**Expected Results:**
   - 1. Form ter-render
   - 2. Field terisi
   - 3. Redirect ke dashboard admin office

---

### TC-2: 🟡 PENDING — Login sebagai mahasiswa dengan kredensial valid

- **Sub Menu**: Login
- **Priority**: 🔴 High
- **Description**: Positive case
- **Precondition**: 1. Berada di halaman login

**Steps:**
   1. Buka /login
   2. Isi username & password mahasiswa
   3. Klik tombol Login

**Expected Results:**
   - 1. Form ter-render
   - 2. Field terisi
   - 3. Redirect ke /home

---

### TC-3: 🟡 PENDING — Login sebagai dosen dengan kredensial valid

- **Sub Menu**: Login
- **Priority**: 🟡 Normal
- **Description**: Positive case
- **Precondition**: 1. Berada di halaman login

**Steps:**
   1. Buka /login
   2. Isi username & password dosen
   3. Klik tombol Login

**Expected Results:**
   - 1. Form ter-render
   - 2. Field terisi
   - 3. Redirect ke /E-Campus

---

### TC-4: 🟡 PENDING — Login sebagai kaprodi dengan kredensial valid

- **Sub Menu**: Login
- **Priority**: 🟡 Normal
- **Description**: Positive case
- **Precondition**: 1. Berada di halaman login

**Steps:**
   1. Buka /login
   2. Isi username & password kaprodi
   3. Klik tombol Login

**Expected Results:**
   - 1. Form ter-render
   - 2. Field terisi
   - 3. Redirect ke /Adminkaprodi

---

### TC-5: 🟡 PENDING — Logout dari dashboard admin office

- **Sub Menu**: Logout
- **Priority**: 🔴 High
- **Description**: Positive case
- **Precondition**: 1. User sudah login sebagai admin office

**Steps:**
   1. Klik dropdown profile
   2. Klik Sign Out

**Expected Results:**
   - 1. Dropdown muncul
   - 2. Redirect ke /login

---
