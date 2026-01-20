import streamlit as st

# ======================
# IMPORT HALAMAN
# ======================
from upload import upload_page
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
# HILANGKAN SIDEBAR TOTAL
# ======================
st.markdown("""
<style>
section[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# ======================
# GLOBAL UI / UX STYLE (COLOR PALETTE)
# ======================
st.markdown("""
<style>

/* ===== GLOBAL BACKGROUND ===== */
.stApp {
    background-color: #F3EEF1;
    color: #2E2E2E;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

/* ===== HEADER ===== */
h1, h2, h3 {
    color: #D56989;
    font-weight: 700;
}

/* ===== TEXT ===== */
p, span, label {
    color: #444444;
}

/* ===== INFO / ALERT BOX ===== */
div[data-testid="stAlert"] {
    background-color: #C2DC80 !important;
    color: #2E2E2E !important;
    border-radius: 14px;
    border: none;
}

/* ===== BUTTON ===== */
button[kind="primary"] {
    background-color: #EA9CAF !important;
    color: white !important;
    border-radius: 10px;
    border: none;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
}

button[kind="primary"]:hover {
    background-color: #D56989 !important;
    color: white !important;
}

/* ===== FILE UPLOADER ===== */
div[data-testid="stFileUploader"] {
    background-color: white;
    border-radius: 14px;
    padding: 1rem;
    border: 1px dashed #D56989;
}

/* ===== TABS ===== */
button[data-baseweb="tab"] {
    font-weight: 600;
    color: #D56989;
}

button[data-baseweb="tab"][aria-selected="true"] {
    border-bottom: 3px solid #D56989;
    color: #D56989;
}

/* ===== DATAFRAME ===== */
div[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
}

/* ===== METRIC CARD ===== */
div[data-testid="metric-container"] {
    background-color: white;
    border-radius: 16px;
    padding: 1rem;
    border: 1px solid #EA9CAF;
}

</style>
""", unsafe_allow_html=True)

# ======================
# HEADER UTAMA (DESIGNER MODE)
# ======================
st.title("Machine Learning Classification Dashboard")

st.caption(
    "Dashboard analisis dan klasifikasi data kesehatan dan lingkungan "
    "menggunakan beberapa algoritma Machine Learning."
)

st.markdown(
    "<div style='height:8px'></div>",
    unsafe_allow_html=True
)

st.info(
    "Proyek Akhir UAS – Mata Kuliah Machine Learning | "
    "Program Studi Sains Data"
)

st.markdown("---")

# ======================
# TAB NAVIGASI (ALUR ML)
# ======================
tabs = st.tabs([
    "Upload Dataset",
    "About Dataset",
    "Exploratory Data Analysis",
    "Machine Learning",
    "Analisis Model",
    "Prediction",
    "Contact"
])

# ======================
# ISI TAB
# ======================
with tabs[0]:
    upload_page()

with tabs[1]:
    show_about()

with tabs[2]:
    dashboard_page()

with tabs[3]:
    modeling_page()

with tabs[4]:
    analysis_model_page()

with tabs[5]:
    prediction_page()

with tabs[6]:
    contact_page()
