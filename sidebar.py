import streamlit as st
import pandas as pd

def sidebar_upload():
    st.sidebar.title("Upload Dataset")

    uploaded_file = st.sidebar.file_uploader(
        "Upload file CSV",
        type=["csv"]
    )

    if uploaded_file is not None:
        # =========================
        # READ CSV (AUTO DELIMITER + ERROR HANDLING)
        # =========================
        try:
            df = pd.read_csv(uploaded_file, sep=None, engine="python")
        except Exception as e:
            st.sidebar.error(f"Gagal membaca file CSV: {e}")
            return

        # =========================
        # SIMPAN KE SESSION STATE
        # =========================
        st.session_state["df"] = df
        st.session_state["dataset_name"] = uploaded_file.name

        # =========================
        # AUTO-DETECT DATASET BERDASARKAN KOLOM
        # =========================
        columns_lower = df.columns.str.lower()

        if "potability" in columns_lower:
            st.session_state["target_col"] = "Potability"
            st.session_state["dataset_type"] = "Lingkungan"

        elif "cardio" in columns_lower:
            st.session_state["target_col"] = "cardio"
            st.session_state["dataset_type"] = "Kesehatan"

        else:
            st.sidebar.error(
                "Dataset tidak dikenali ❌\n\n"
                "Pastikan dataset memiliki kolom target:\n"
                "- `Potability` (Lingkungan)\n"
                "- `cardio` (Kesehatan)"
            )
            return

        # =========================
        # FEEDBACK BERHASIL
        # =========================
        st.sidebar.success("Dataset berhasil dimuat ✅")

        # =========================
        # PREVIEW DATA (NILAI PLUS)
        # =========================
        st.sidebar.markdown("### 🔍 Preview Dataset")
        st.sidebar.dataframe(df.head())
