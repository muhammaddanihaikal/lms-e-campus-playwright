"""Helper untuk lokasi file test (PDF, ZIP, dsb)."""

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
FILES_DIR = ROOT_DIR / "tests" / "files"
LEGACY_FILES_DIR = ROOT_DIR / "test" / "files"
DATA_DIR = ROOT_DIR / "data"


def file_path(name: str) -> str:
    """Return absolute path string ke file di folder tests/files."""
    candidate = FILES_DIR / name
    if candidate.exists():
        return str(candidate)
    legacy = LEGACY_FILES_DIR / name
    if legacy.exists():
        return str(legacy)
    return str(candidate)
