import streamlit as st
import pandas as pd


def show_about():

    # =========================
    # STYLE KHUSUS ABOUT PAGE
    # =========================
    st.markdown("""
    <style>
    /* Background section */
    .about-card {
        background-color: #E7BEF8;
        padding: 24px;
        border-radius: 18px;
        margin-bottom: 24px;
    }

    /* Heading */
    .about-title {
        color: #F2619C;
        font-weight: 700;
    }

    /* Highlight / Info box */
    div[data-testid="stAlert"] {
        background-color: #EDE986 !important;
        color: #2E2E2E !important;
        border-radius: 14px;
        border: none;
    }

    /* Metric card */
    div[data-testid="metric-container"] {
        background-color: #93ABD9;
        border-radius: 16px;
        padding: 1rem;
        color: #ffffff;
        border: none;
    }

    /* Dataframe */
    div[data-testid="stDataFrame"] {
        border-radius: 16px;
        overflow: hidden;
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # PENGAMAN (SESSION STATE)
    # =========================
    if "df" not in st.session_state:
        st.warning("Silakan upload dataset terlebih dahulu pada menu Upload Data.")
        return

    df = st.session_state["df"]
    dataset_name = st.session_state.get("dataset_name", "Tidak diketahui")

    # =========================
    # DESKRIPSI DATASET
    # =========================
    st.markdown("<h2 class='about-title'>Informasi Umum Dataset</h2>", unsafe_allow_html=True)

    st.markdown("<div class='about-card'>", unsafe_allow_html=True)

    if dataset_name == "water_potability.csv":
        st.markdown("""
        **Water Potability Dataset** digunakan untuk
        melakukan **klasifikasi kelayakan air minum**
        berdasarkan parameter kualitas air fisik dan kimia.

        **Fitur utama yang digunakan:**
        - pH  
        - Hardness  
        - Solids  
        - Chloramines  
        - Sulfate  
        - Conductivity  
        - Organic Carbon  
        - Trihalomethanes  
        - Turbidity  

        **Target Variabel:**
        - `Potability`  
          - 0 → Air tidak layak konsumsi  
          - 1 → Air layak konsumsi  

        **Jenis Permasalahan:**
        - Supervised Learning  
        - Binary Classification
        """)
        dataset_type = "Lingkungan"

    elif dataset_name == "cardio_train.csv":
        st.markdown("""
        **Cardiovascular Disease Dataset** digunakan untuk
        memprediksi **risiko penyakit kardiovaskular**
        berdasarkan data klinis dan gaya hidup pasien.

        **Fitur utama yang digunakan:**
        - Usia  
        - Jenis Kelamin  
        - Tekanan Darah  
        - Kolesterol  
        - Glukosa  
        - Indeks Massa Tubuh (BMI)  
        - Kebiasaan Merokok  
        - Aktivitas Fisik  

        **Target Variabel:**
        - `cardio`  
          - 0 → Tidak berisiko  
          - 1 → Berisiko  

        **Jenis Permasalahan:**
        - Supervised Learning  
        - Binary Classification
        """)
        dataset_type = "Kesehatan"

    else:
        st.markdown("""
        Dataset diunggah oleh pengguna.

        Informasi target dan tipe permasalahan
        akan ditentukan pada tahap **Machine Learning**.
        """)
        dataset_type = "Tidak diketahui"

    st.markdown("</div>", unsafe_allow_html=True)

    # =========================
    # RINGKASAN DATASET
    # =========================
    st.markdown("<h3 class='about-title'>Ringkasan Dataset</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Jumlah Data", df.shape[0])
    col2.metric("Jumlah Fitur", df.shape[1])
    col3.metric("Jenis Dataset", dataset_type)

    # =========================
    # PREVIEW DATA
    # =========================
    st.markdown("<h3 class='about-title'>Preview Data</h3>", unsafe_allow_html=True)
    st.dataframe(df.head(), use_container_width=True)

    # =========================
    # METODE ML
    # =========================
    st.markdown("<h3 class='about-title'>Metode Machine Learning</h3>", unsafe_allow_html=True)

    st.markdown("""
    Aplikasi ini menerapkan beberapa algoritma
    **Machine Learning untuk klasifikasi**, yaitu:

    - Logistic Regression  
    - Decision Tree  
    - Random Forest  
    - Support Vector Machine (SVM)  
    - CatBoost Classifier  

    Evaluasi performa model menggunakan:
    Accuracy, Precision, Recall, F1-Score, dan ROC-AUC.
    """)

    # =========================
    # CATATAN
    # =========================
    st.info(
        "Catatan:\n"
        "- Dataset akan melalui tahap preprocessing sebelum pemodelan.\n"
        "- Preprocessing meliputi penanganan missing value dan standarisasi fitur.\n"
        "- Target variabel ditentukan secara otomatis.\n"
        "- Hasil evaluasi model ditampilkan pada menu Machine Learning."
    )
