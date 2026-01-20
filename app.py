import streamlit as st

# ======================
# IMPORT HALAMAN & SIDEBAR
# ======================
from sidebar import sidebar_upload

from about import show_about
from dashboard import dashboard_page
from modeling import modeling_page
from analysis_model import analysis_model_page
from prediction import prediction_page
from contact import contact_page


# ======================
# KONFIGURASI HALAMAN
# ======================
st.set_page_config(
    page_title="Machine Learning Classification Dashboard",
    layout="wide"
)

# ======================
# SIDEBAR (UPLOAD DATASET)
# ======================
sidebar_upload()

# ======================
# JUDUL & DESKRIPSI UTAMA
# ======================
st.title("Machine Learning Classification Dashboard")

st.caption(
    "Aplikasi analisis dan klasifikasi data kesehatan dan lingkungan "
    "menggunakan beberapa algoritma Machine Learning. "
    "Aplikasi ini mendukung proses eksplorasi data, pelatihan model, "
    "evaluasi performa, serta prediksi data baru secara interaktif."
)

st.markdown("---")

st.info(
    "Proyek Akhir UAS – Mata Kuliah Machine Learning | "
    "Program Studi Sains Data"
)

# ======================
# PENGAMAN GLOBAL DATASET (OPSIONAL TAPI AMAN)
# ======================
if "df" not in st.session_state:
    st.warning(
        "Silakan upload dataset terlebih dahulu melalui sidebar "
        "untuk mengakses seluruh fitur aplikasi."
    )

# ======================
# MENU TAB APLIKASI
# ======================
tabs = st.tabs([
    "About Dataset",
    "Dashboards",
    "Machine Learning",
    "Analisis Mekanisme Model",
    "Prediction App",
    "Contact Me"
])

# ======================
# ISI TIAP TAB
# ======================
with tabs[0]:
    show_about()

with tabs[1]:
    dashboard_page()

with tabs[2]:
    modeling_page()

with tabs[3]:
    analysis_model_page()

with tabs[4]:
    prediction_page()

with tabs[5]:
    contact_page()
