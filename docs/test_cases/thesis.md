# Test Cases — Thesis Flow

### TC-17: 🟡 PENDING — Submit proposal thesis sebagai student

- **Sub Menu**: Student / Thesis
- **Priority**: 🔴 High
- **Description**: Positive case
- **Precondition**: 1. Student belum pernah submit proposal

**Steps:**
   1. Login student
   2. Buka menu Thesis
   3. Klik Start Thesis Proposal
   4. Isi form proposal (track, title, advisor, background, objectives, methodology)
   5. Upload PDF proposal
   6. Submit

**Expected Results:**
   - 1. Login sukses
   - 2. Menu Thesis terbuka
   - 3. Form proposal muncul
   - 4. Field terisi
   - 5. File ter-upload
   - 6. Tombol Start Thesis Proposal hilang (proposal tersimpan)

---

### TC-18: 🟡 PENDING — Approve proposal thesis di tab Pending

- **Sub Menu**: Kaprodi / Proposal Approval
- **Priority**: 🔴 High
- **Description**: Positive case
- **Precondition**: 1. Proposal sudah disubmit student

**Steps:**
   1. Login kaprodi
   2. Buka Thesis Management → Proposal Approval
   3. Pilih tab Pending
   4. Pilih proposal target → Approve
   5. Pilih advisor & isi catatan
   6. Konfirmasi Approve Proposal

**Expected Results:**
   - 1. Login sukses
   - 2. Halaman Proposal Approval terbuka
   - 3. Tab Pending aktif
   - 4. Modal terbuka
   - 5. Field terisi
   - 6. Proposal pindah ke tab Approved

---

### TC-19: 🟡 PENDING — Approve research progress student

- **Sub Menu**: Lecturer / Student Thesis Progress
- **Priority**: 🔴 High
- **Description**: Positive case
- **Precondition**: 1. Proposal sudah di-approve kaprodi

**Steps:**
   1. Login dosen
   2. Buka Student Thesis Progress
   3. Buka detail student bimbingan
   4. Buka tab Research → Approve
   5. Isi catatan → Approve & Continue

**Expected Results:**
   - 1. Login sukses
   - 2. Halaman terbuka
   - 3. Detail muncul
   - 4. Modal Approve muncul
   - 5. Toast sukses

---

### TC-20: 🟡 PENDING — Submit defense request dengan file ZIP

- **Sub Menu**: Student / Defense
- **Priority**: 🔴 High
- **Description**: Positive case
- **Precondition**: 1. Research sudah di-approve dosen

**Steps:**
   1. Login student
   2. Buka menu Thesis → Defense
   3. Klik Submit Defense Request
   4. Upload file ZIP
   5. Submit Request

**Expected Results:**
   - 1. Login sukses
   - 2. Menu Defense aktif
   - 3. Modal terbuka
   - 4. ZIP ter-upload
   - 5. Tombol Submit Defense Request hilang

---

### TC-21: 🟡 PENDING — Approve defense request di tab Submitted

- **Sub Menu**: Kaprodi / Defense Documents
- **Priority**: 🔴 High
- **Description**: Positive case
- **Precondition**: 1. Defense request sudah disubmit student

**Steps:**
   1. Login kaprodi
   2. Buka Thesis Management → Defense Documents
   3. Pilih tab Submitted
   4. Pilih defense request student
   5. Klik Review → Accept Defense Request

**Expected Results:**
   - 1. Login sukses
   - 2. Halaman terbuka
   - 3. Tab Submitted aktif
   - 4. Modal Review terbuka
   - 5. Defense pindah ke tab Approved

---
