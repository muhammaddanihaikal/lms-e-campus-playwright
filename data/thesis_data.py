"""
Data untuk Thesis
"""


def thesis_proposal_data(student_name: str = "student"):
    """Generate data proposal thesis
    
    Args:
        student_name: Nama student untuk personalisasi judul
        
    Returns:
        dict: Data proposal thesis
    """
    return {
        "thesis_track": "Thesis",  # Value yang benar
        "thesis_title": f"Tesis Sistem Informasi {student_name}",
        "research_background": "Sistem informasi penting untuk efisiensi bisnis modern",
        "research_objectives": "Menganalisis dampak sistem informasi terhadap produktivitas",
        "methodology": "Kualitatif dengan studi kasus"
    }


def approval_data():
    """Generate data approval proposal
    
    Returns:
        dict: Data approval
    """
    return {
        "advisor": "2901",  # Sesuaikan dengan option yang tersedia
        "approval_note": "Proposal disetujui, silakan lanjutkan penelitian"
    }
