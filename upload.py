import streamlit as st
import pandas as pd


def upload_page():
    st.subheader("Upload Dataset")

    st.write(
        "Unggah dataset dalam format **CSV** untuk memulai "
        "proses analisis dan pemodelan Machine Learning."
    )

    uploaded_file = st.file_uploader(
        "Upload file CSV",
        type=["csv"],
        label_visibility="collapsed"
    )

    if uploaded_file is not None:

        # =========================
        # BACA CSV (AUTO DELIMITER)
        # =========================
        try:
            df = pd.read_csv(uploaded_file, sep=None, engine="python")
        except Exception:
            st.error("❌ Dataset gagal dibaca. Pastikan format CSV benar.")
            return

        # =========================
        # RESET STATE LAMA (PENTING!)
        # =========================
        keys_to_reset = [
            "best_model",
            "scaler",
            "feature_columns",
            "target_col",
            "dataset_type"
        ]

        for key in keys_to_reset:
            if key in st.session_state:
                del st.session_state[key]

        # =========================
        # SIMPAN DATASET
        # =========================
        st.session_state["df"] = df
        st.session_state["dataset_name"] = uploaded_file.name

        # =========================
        # TARGET & TIPE DATASET
        # =========================
        if uploaded_file.name == "water_potability.csv":
            st.session_state["target_col"] = "Potability"
            st.session_state["dataset_type"] = "Lingkungan"

        elif uploaded_file.name == "cardio_train.csv":
            st.session_state["target_col"] = "cardio"
            st.session_state["dataset_type"] = "Kesehatan"

        else:
            st.warning(
                "Dataset berhasil dimuat, tetapi target belum dikenali. "
                "Silakan pastikan struktur dataset sesuai."
            )

        # =========================
        # FEEDBACK KE USER
        # =========================
        st.success("✅ Dataset berhasil dimuat dan state diperbarui")

        with st.expander("🔍 Lihat 5 Baris Pertama Dataset"):
            st.dataframe(
                df.head(),
                use_container_width=True
            )
