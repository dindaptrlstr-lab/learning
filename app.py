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
# GLOBAL UI / UX STYLE (PALETTE BARU)
# ======================
st.markdown("""
<style>

/* ===== GLOBAL ===== */
.stApp {
    background-color: #E7BEF8; /* Soft Lilac */
    color: #2E2E2E;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

/* ===== HEADER ===== */
h1, h2, h3 {
    color: #F2619C; /* Raspberry Rose */
    font-weight: 700;
}

/* ===== TEXT ===== */
p, span, label {
    color: #333333;
}

/* ===== INFO / ALERT ===== */
div[data-testid="stAlert"] {
    background-color: #EDE986 !important; /* Lemon Cream */
    color: #2E2E2E !important;
    border-radius: 16px;
    border: none;
}

/* ===== SUCCESS ===== */
div[data-testid="stSuccess"] {
    background-color: #93ABD9 !important; /* Blueberry Milk */
    color: #ffffff !important;
    border-radius: 16px;
    border: none;
}

/* ===== BUTTON ===== */
button[kind="primary"] {
    background-color: #F2619C !important;
    color: white !important;
    border-radius: 12px;
    border: none;
    padding: 0.6rem 1.4rem;
    font-weight: 600;
}

button[kind="primary"]:hover {
    background-color: #93ABD9 !important;
    color: white !important;
}

/* ===== FILE UPLOADER ===== */
div[data-testid="stFileUploader"] {
    background-color: white;
    border-radius: 16px;
    padding: 1rem;
    border: 1.5px dashed #F2619C;
}

/* ===== TABS ===== */
button[data-baseweb="tab"] {
    font-weight: 600;
    color: #F2619C;
}

button[data-baseweb="tab"][aria-selected="true"] {
    border-bottom: 3px solid #F2619C;
    color: #F2619C;
}

/* ===== DATAFRAME ===== */
div[data-testid="stDataFrame"] {
    background-color: white;
    border-radius: 16px;
    overflow: hidden;
}

/* ===== METRIC CARD ===== */
div[data-testid="metric-container"] {
    background-color: #93ABD9;
    color: white;
    border-radius: 18px;
    padding: 1rem;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# ======================
# HEADER UTAMA
# ======================
st.title("Machine Learning Classification Dashboard")

st.caption(
    "Dashboard analisis dan klasifikasi data kesehatan dan lingkungan "
    "menggunakan beberapa algoritma Machine Learning."
)

st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

st.info(
    "Proyek Akhir UAS – Mata Kuliah Machine Learning | "
    "Program Studi Sains Data"
)

st.markdown("---")

# ======================
# TAB NAVIGASI
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
