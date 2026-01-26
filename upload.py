import streamlit as st
import pandas as pd
import os


def upload_page():

    # =========================
    # HEADER
    # =========================
    st.subheader("Pilih Dataset")

    st.write(
        "Pilih dataset yang akan digunakan sebagai dasar "
        "analisis dan pemodelan Machine Learning."
    )

    st.markdown("---")

    # =========================
    # DATASET CONFIG
    # =========================
    datasets = {
        "Water Potability Dataset": {
            "description": "Dataset kualitas air untuk klasifikasi kelayakan air minum.",
            "target": "Potability",
            "domain": "Lingkungan",
            "file": "water_potability.csv"
        },
        "Cardiovascular Disease Dataset": {
            "description": "Dataset klinis untuk klasifikasi risiko penyakit jantung.",
            "target": "cardio",
            "domain": "Kesehatan",
            "file": "cardio_train.csv"
        }
    }

    # =========================
    # PILIH DATASET
    # =========================
    selected_name = st.radio(
        "Dataset tersedia",
        list(datasets.keys())
    )

    selected = datasets[selected_name]

    # =========================
    # DESKRIPSI DATASET
    # =========================
    st.markdown(
        f"""
        **Deskripsi Dataset**  
        {selected["description"]}

        **Domain:** {selected["domain"]}  
        **Target Variabel:** `{selected["target"]}`
        """
    )

    st.markdown("---")

    # =========================
    # TOMBOL AKSI
    # =========================
    if st.button("Gunakan Dataset"):
        load_dataset(selected, selected_name)


def load_dataset(config, name):

    # =========================
    # CEK FILE
    # =========================
    if not os.path.exists(config["file"]):
        st.error(f"File `{config['file']}` tidak ditemukan.")
        return

    # =========================
    # LOAD DATA
    # =========================
    df = pd.read_csv(config["file"], sep=None, engine="python")

    # =========================
    # RESET STATE
    # =========================
    for key in ["best_model", "scaler", "feature_columns"]:
        if key in st.session_state:
            del st.session_state[key]

    # =========================
    # SIMPAN STATE
    # =========================
    st.session_state["df"] = df
    st.session_state["dataset_name"] = config["file"]
    st.session_state["target_col"] = config["target"]
    st.session_state["dataset_type"] = config["domain"]

    # =========================
    # FEEDBACK
    # =========================
    st.success(f"Dataset **{name}** berhasil dimuat")

    with st.expander("Lihat 5 baris pertama dataset"):
        st.dataframe(df.head(), use_container_width=True)
