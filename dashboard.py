import streamlit as st
import plotly.express as px
import pandas as pd

def dashboard_page():

    # =========================
    # PENGAMAN SUPER KETAT
    # =========================
    required_keys = ["df", "dataset_type", "target_col"]
    for key in required_keys:
        if key not in st.session_state:
            st.warning("Silakan upload dataset terlebih dahulu.")
            return

    df = st.session_state["df"]
    dataset_type = st.session_state["dataset_type"]
    target_col = st.session_state["target_col"]

    # 🔴 ANTI KEYERROR
    if target_col not in df.columns:
        st.error("❌ ERROR TARGET COLUMN")
        st.write("Kolom tersedia di dataset:")
        st.write(list(df.columns))
        st.write("Target yang dicari:", target_col)
        return

    # =========================
    # JUDUL & DESKRIPSI
    # =========================
    st.title("Dashboards & Exploratory Data Analysis")

    st.write("""
    Halaman ini menampilkan **Exploratory Data Analysis (EDA)** untuk memahami
    karakteristik dataset sebelum dilakukan pemodelan Machine Learning.
    Analisis dilakukan menggunakan visualisasi distribusi target
    dan hubungan antar fitur numerik.
    """)

    st.markdown("---")

    # =========================
    # METRIC
    # =========================
    total_data = len(df)
    positive_count = int(df[target_col].sum())
    positive_rate = (positive_count / total_data) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Data", total_data)
    col2.metric("Jumlah Target = 1", positive_count)
    col3.metric("Persentase", f"{positive_rate:.2f}%")

    st.markdown("---")

    # =========================
    # VISUAL TARGET
    # =========================
    fig = px.pie(
        df,
        names=target_col,
        title=f"Distribusi Target `{target_col}`"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.write("""
     **Insight:**
    Visualisasi distribusi target menunjukkan proporsi masing-masing kelas.
    Distribusi yang tidak seimbang dapat memengaruhi performa model,
    sehingga evaluasi tidak hanya mengandalkan akurasi, tetapi juga
    precision, recall, dan F1-score.
    """)

    st.markdown("---")

    # =========================
    # HEATMAP KORELASI
    # =========================
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.shape[1] > 1:
        fig = px.imshow(
            numeric_df.corr(),
            text_auto=True,
            title="Heatmap Korelasi Fitur Numerik"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.write("""
         **Insight:**
        Heatmap korelasi digunakan untuk mengidentifikasi hubungan antar fitur numerik.
        Korelasi yang tinggi dapat mengindikasikan redundansi fitur,
        sedangkan korelasi rendah menunjukkan kontribusi fitur yang lebih independen
        dalam proses klasifikasi.
        """)
