import streamlit as st
import pandas as pd
import numpy as np
from scipy.special import expit  # sigmoid stabil numerik


def analysis_model_page():

    # =========================
    # STYLE (COLOR PALETTE)
    # =========================
    st.markdown("""
    <style>
    .analysis-card {
        background-color: #E7BEF8;
        padding: 24px;
        border-radius: 18px;
        margin-bottom: 24px;
    }

    .analysis-title {
        color: #F2619C;
        font-weight: 700;
    }

    /* Info box */
    div[data-testid="stAlert"] {
        background-color: #EDE986 !important;
        color: #2E2E2E !important;
        border-radius: 14px;
        border: none;
    }

    /* Success box */
    div[data-testid="stSuccess"] {
        background-color: #93ABD9 !important;
        color: #ffffff !important;
        border-radius: 14px;
        border: none;
    }

    /* Selectbox */
    div[data-baseweb="select"] {
        background-color: white;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # PENGAMAN DATASET
    # =====================================================
    if "df" not in st.session_state or "dataset_name" not in st.session_state:
        st.warning("Silakan upload dataset terlebih dahulu pada menu Upload Data.")
        return

    df = st.session_state["df"]
    dataset_name = st.session_state["dataset_name"]

    # =====================================================
    # TARGET OTOMATIS
    # =====================================================
    if dataset_name == "water_potability.csv":
        target_col = "Potability"
        dataset_type = "Lingkungan"
    elif dataset_name == "cardio_train.csv":
        target_col = "cardio"
        dataset_type = "Kesehatan"
    else:
        st.error("Dataset tidak dikenali.")
        return

    # =====================================================
    # HEADER
    # =====================================================
    st.markdown(
        "<h2 class='analysis-title'>Analisis Model Klasifikasi</h2>",
        unsafe_allow_html=True
    )

    st.write(
        f"Dataset: **{dataset_name}** ({dataset_type})  \n"
        "Halaman ini menampilkan **mekanisme internal dan ilustrasi perhitungan** "
        "algoritma Machine Learning."
    )

    st.markdown("<div class='analysis-card'>", unsafe_allow_html=True)
    st.markdown("""
    Halaman ini bersifat **edukatif**, bertujuan menjelaskan
    **cara kerja algoritma klasifikasi** secara konseptual dan matematis.

    Perhitungan yang ditampilkan **bukan hasil training aktual**,
    melainkan simulasi sederhana untuk membantu pemahaman logika model.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # PILIH ALGORITMA
    # =====================================================
    algo = st.selectbox(
        "Pilih Algoritma Klasifikasi",
        [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "Support Vector Machine (SVM)",
            "CatBoost"
        ]
    )

    # =====================================================
    # SAMPLE DATA NUMERIK
    # =====================================================
    numeric_df = df.select_dtypes(include="number").drop(
        columns=[target_col], errors="ignore"
    )

    if numeric_df.empty:
        st.error("Dataset tidak memiliki fitur numerik.")
        return

    X_sample = numeric_df.iloc[0].values

    # =====================================================
    # LOGISTIC REGRESSION
    # =====================================================
    if algo == "Logistic Regression":
        st.markdown("<h3 class='analysis-title'>Logistic Regression</h3>", unsafe_allow_html=True)

        beta = np.ones(len(X_sample)) * 0.1
        beta_0 = 0.1

        z = beta_0 + np.dot(X_sample, beta)
        prob = expit(z)
        kelas = 1 if prob >= 0.5 else 0

        st.write("**Model:**  z = β₀ + β·x")
        st.write(f"z = `{z:.4f}`")
        st.write(f"Sigmoid(z) = `{prob:.4f}`")
        st.success(f"Prediksi Kelas: **{kelas}**")

        st.info(
            "Logistic Regression memetakan kombinasi linear fitur "
            "ke probabilitas menggunakan fungsi sigmoid."
        )

    # =====================================================
    # DECISION TREE
    # =====================================================
    elif algo == "Decision Tree":
        st.markdown("<h3 class='analysis-title'>Decision Tree</h3>", unsafe_allow_html=True)

        p = df[target_col].value_counts(normalize=True)
        entropy = -(p * np.log2(p)).sum()

        feature = numeric_df.columns[0]
        threshold = df[feature].median()

        st.write(f"Entropy Awal Dataset: `{entropy:.4f}`")
        st.write(f"Fitur Contoh: `{feature}`")
        st.write(f"Threshold (Median): `{threshold:.4f}`")

        st.success("Fitur dipilih berdasarkan Information Gain tertinggi.")

        st.info(
            "Decision Tree memilih fitur pemisah terbaik "
            "untuk memaksimalkan pemisahan kelas."
        )

    # =====================================================
    # RANDOM FOREST
    # =====================================================
    elif algo == "Random Forest":
        st.markdown("<h3 class='analysis-title'>Random Forest</h3>", unsafe_allow_html=True)

        fake_preds = np.random.choice(df[target_col].unique(), size=7)
        vote = pd.Series(fake_preds).value_counts().idxmax()

        st.write("Prediksi dari beberapa tree:")
        st.write(fake_preds)

        st.success(f"Hasil Voting Mayoritas: **{vote}**")

        st.info(
            "Random Forest menggabungkan banyak Decision Tree "
            "untuk meningkatkan stabilitas prediksi."
        )

    # =====================================================
    # SVM
    # =====================================================
    elif algo == "Support Vector Machine (SVM)":
        st.markdown("<h3 class='analysis-title'>Support Vector Machine</h3>", unsafe_allow_html=True)

        w = np.ones(len(X_sample)) * 0.5
        b = -0.2

        decision_value = np.dot(w, X_sample) + b
        kelas = 1 if decision_value >= 0 else 0

        st.write(f"Decision Function: `{decision_value:.4f}`")
        st.success(f"Hasil Klasifikasi: **{kelas}**")

        st.info(
            "SVM mengklasifikasikan data berdasarkan "
            "posisi relatif terhadap hyperplane."
        )

    # =====================================================
    # CATBOOST
    # =====================================================
    elif algo == "CatBoost":
        st.markdown("<h3 class='analysis-title'>CatBoost</h3>", unsafe_allow_html=True)

        initial = 0.5
        learning_rate = 0.1
        correction = -0.2

        updated = initial + learning_rate * correction

        st.write(f"Prediksi Awal: `{initial}`")
        st.write(f"Prediksi Baru: `{updated:.4f}`")

        st.success("Prediksi diperbarui melalui mekanisme boosting.")

        st.info(
            "CatBoost merupakan algoritma gradient boosting "
            "yang efektif untuk data tabular."
        )

    # =====================================================
    # CATATAN PENUTUP
    # =====================================================
    st.info(
        "Perhitungan pada halaman ini bersifat **edukatif**. "
        "Training dan evaluasi model sebenarnya "
        "dilakukan pada menu **Machine Learning**."
    )
