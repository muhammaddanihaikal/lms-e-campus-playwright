# E2E Test Cases Documentation

## TC-21: E2E Thesis Full Flow (State-Machine)
**File**: `tests/thesis/test_thesis_full_flow.py::test_thesis_full_flow`

**Description**: Complete thesis journey across multiple roles with state-machine pattern.
- Login → detect current state → execute remaining phases (idempotent)
- Student submit proposal → Kaprodi approve → Lecturer approve research → Student submit defense → Kaprodi approve defense

**State Flow**:
```
NO_PROPOSAL → PROPOSAL_SUBMITTED → DEFENSE_READY → DEFENSE_SUBMITTED → COMPLETED
```

**Fixtures**: `login_credentials`, `thesis_actors`
**Roles**: student, kaprodi, lecturer

---

## TC-22: Student E2E - Submit Proposal & Check Status
**File**: `tests/e2e/test_student_e2e.py::test_student_thesis_journey`

**Description**: Student complete thesis proposal submission journey.
1. Login as student
2. Navigate to thesis
3. Submit proposal (if not submitted; skip if already submitted)
4. Verify status (tombol Start hilang)
5. Logout

**Fixtures**: `student_e2e_actors`, `login_credentials`
**Role**: student
**Idempotent**: Yes (skip if already submitted)

---

## TC-23: Kaprodi E2E - Navigate & Approve Proposals
**File**: `tests/e2e/test_kaprodi_e2e.py::test_kaprodi_approval_journey`

**Description**: Kaprodi complete proposal approval journey.
1. Login as kaprodi
2. Navigate to Proposal Approval
3. Check pending proposals tab
4. Find & approve proposal (if exists; skip if none)
5. Verify moved to Approved tab
6. Logout

**Fixtures**: `kaprodi_e2e_actors`, `login_credentials`
**Role**: kaprodi
**Idempotent**: Yes (skip if no pending proposals)

---

## TC-24: Lecturer E2E - Navigate & Approve Research
**File**: `tests/e2e/test_lecturer_e2e.py::test_lecturer_research_journey`

**Description**: Lecturer complete research progress approval journey.
1. Login as lecturer
2. Navigate to Student Thesis Progress
3. Find student row
4. Open progress modal & approve research
5. Verify approval (idempotent)
6. Logout

**Fixtures**: `lecturer_e2e_actors`, `login_credentials`
**Role**: lecturer
**Idempotent**: Yes (pass regardless of previous approval)

---

## TC-25: Admin Office E2E - Student CRUD Journey
**File**: `tests/e2e/test_admin_office_e2e.py::test_admin_office_student_crud_journey`

**Description**: Admin Office complete student lifecycle (CRUD).
1. Login as admin office
2. Add new student
3. View student details & verify
4. Edit student (name, email, phone, address)
5. Verify edit
6. Delete student
7. Verify deletion
8. Logout

**Fixtures**: `admin_office_e2e_actors`, `login_credentials`
**Role**: admin_office
**Idempotent**: No (creates, modifies, deletes real data)

---

## Notes

- All E2E tests follow complete user journeys (login → navigate → execute → logout)
- Idempotent tests skip automatically if preconditions already met
- Tests use faker_helper for dynamic data generation
- State-machine pattern used where applicable (thesis flow)
