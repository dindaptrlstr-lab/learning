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
        df = pd.read_csv(uploaded_file)

        st.session_state["df"] = df
        st.session_state["dataset_name"] = uploaded_file.name

        st.success("✅ Dataset berhasil dimuat")

        with st.expander("🔍 Lihat Contoh Data"):
            st.dataframe(df.head(), use_container_width=True)
