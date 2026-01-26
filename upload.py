import streamlit as st
import pandas as pd
import os


def upload_page():

    # =========================
    # TITLE
    # =========================
    st.subheader("Pilih Dataset")

    st.write(
        "Pilih dataset yang akan digunakan sebagai dasar "
        "analisis dan pemodelan **Machine Learning**."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================
    # CARD STYLE
    # =========================
    st.markdown("""
    <style>
    .dataset-card {
        background-color: #E7BEF8;
        padding: 24px;
        border-radius: 18px;
        height: 100%;
    }

    .dataset-title {
        color: #F2619C;
        font-weight: 700;
        font-size: 18px;
    }

    .dataset-desc {
        font-size: 14px;
        color: #333333;
        margin-bottom: 12px;
    }

    .dataset-meta {
        font-size: 13px;
        color: #555555;
        margin-bottom: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # DATASET CONFIG
    # =========================
    datasets = {
        "water": {
            "title": "Water Potability Dataset",
            "desc": "Dataset kualitas air untuk menentukan kelayakan air minum.",
            "target": "Potability",
            "type": "Lingkungan",
            "file": "water_potability.csv"
        },
        "cardio": {
            "title": "Cardiovascular Disease Dataset",
            "desc": "Dataset klinis untuk prediksi risiko penyakit jantung.",
            "target": "cardio",
            "type": "Kesehatan",
            "file": "cardio_train.csv"
        }
    }

    col1, col2 = st.columns(2)

    # =========================
    # CARD 1 — WATER
    # =========================
    with col1:
        st.markdown(f"""
        <div class="dataset-card">
            <div class="dataset-title">{datasets['water']['title']}</div>
            <div class="dataset-desc">{datasets['water']['desc']}</div>
            <div class="dataset-meta">
                📌 Domain: {datasets['water']['type']}<br>
                🎯 Target: {datasets['water']['target']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Gunakan Dataset Air", key="water_btn"):
            load_dataset(datasets["water"])

    # =========================
    # CARD 2 — CARDIO
    # =========================
    with col2:
        st.markdown(f"""
        <div class="dataset-card">
            <div class="dataset-title">{datasets['cardio']['title']}</div>
            <div class="dataset-desc">{datasets['cardio']['desc']}</div>
            <div class="dataset-meta">
                📌 Domain: {datasets['cardio']['type']}<br>
                🎯 Target: {datasets['cardio']['target']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Gunakan Dataset Kesehatan", key="cardio_btn"):
            load_dataset(datasets["cardio"])


def load_dataset(config):

    # =========================
    # LOAD FILE
    # =========================
    if not os.path.exists(config["file"]):
        st.error(f"File `{config['file']}` tidak ditemukan.")
        return

    df = pd.read_csv(config["file"], sep=None, engine="python")

    # =========================
    # RESET STATE
    # =========================
    for key in ["best_model", "scaler", "feature_columns"]:
        if key in st.session_state:
            del st.session_state[key]

    # =========================
    # SAVE STATE
    # =========================
    st.session_state["df"] = df
    st.session_state["dataset_name"] = config["file"]
    st.session_state["target_col"] = config["target"]
    st.session_state["dataset_type"] = config["type"]

    # =========================
    # FEEDBACK
    # =========================
    st.success(f"Dataset **{config['title']}** berhasil dimuat")

    with st.expander("🔍 Preview 5 Baris Pertama"):
        st.dataframe(df.head(), use_container_width=True)
