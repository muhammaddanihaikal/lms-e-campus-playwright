from pages.admission_page import AdmissionPage
from data.admission_data import admission_data

def test_admission(page):
    # Buat data dummy
    data = admission_data()

    admission = AdmissionPage(page)
    admission.open()
    admission.submit(data)