import streamlit as st
import pandas as pd
import os


def upload_page():

    st.subheader("Pilih Dataset")

    st.write(
        "Pilih dataset yang akan digunakan untuk proses "
        "**analisis dan pemodelan Machine Learning**."
    )

    # =========================
    # PILIH DATASET
    # =========================
    dataset_option = st.selectbox(
        "Dataset tersedia",
        [
            "Pilih dataset",
            "Water Potability Dataset",
            "Cardiovascular Disease Dataset"
        ]
    )

    # =========================
    # JIKA BELUM PILIH
    # =========================
    if dataset_option == "Pilih dataset":
        st.info("Silakan pilih salah satu dataset untuk melanjutkan.")
        return

    # =========================
    # MAPPING DATASET
    # =========================
    dataset_config = {
        "Water Potability Dataset": {
            "file": "water_potability.csv",
            "target": "Potability",
            "type": "Lingkungan"
        },
        "Cardiovascular Disease Dataset": {
            "file": "cardio_train.csv",
            "target": "cardio",
            "type": "Kesehatan"
        }
    }

    selected = dataset_config[dataset_option]
    file_path = selected["file"]

    # =========================
    # LOAD DATASET
    # =========================
    if not os.path.exists(file_path):
        st.error(f"File `{file_path}` tidak ditemukan di server.")
        return

    df = pd.read_csv(file_path, sep=None, engine="python")

    # =========================
    # RESET STATE LAMA
    # =========================
    keys_to_reset = [
        "best_model",
        "scaler",
        "feature_columns"
    ]

    for key in keys_to_reset:
        if key in st.session_state:
            del st.session_state[key]

    # =========================
    # SIMPAN KE SESSION STATE
    # =========================
    st.session_state["df"] = df
    st.session_state["dataset_name"] = file_path
    st.session_state["target_col"] = selected["target"]
    st.session_state["dataset_type"] = selected["type"]

    # =========================
    # FEEDBACK
    # =========================
    st.success(f"✅ Dataset **{dataset_option}** berhasil dimuat")

    # =========================
    # PREVIEW DATA
    # =========================
    with st.expander("🔍 Lihat 5 Baris Pertama Dataset"):
        st.dataframe(df.head(), use_container_width=True)
