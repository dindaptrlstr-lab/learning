import streamlit as st
import plotly.express as px
import pandas as pd


def dashboard_page():

    required_keys = ["df", "target_col", "dataset_type"]
    for key in required_keys:
        if key not in st.session_state:
            st.warning("Silakan upload dataset terlebih dahulu.")
            return

    df = st.session_state["df"]
    target_col = st.session_state["target_col"]
    dataset_type = st.session_state["dataset_type"]

    if target_col not in df.columns:
        st.error("❌ Target kolom tidak ditemukan pada dataset.")
        st.write("Kolom tersedia:", list(df.columns))
        st.write("Target yang dicari:", target_col)
        return

    st.title("Exploratory Data Analysis (EDA)")
    st.write(f"Jenis Dataset: **{dataset_type}**")

    total_data = len(df)
    positive_count = int(df[target_col].sum())
    positive_rate = (positive_count / total_data) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Data", total_data)
    col2.metric("Target = 1", positive_count)
    col3.metric("Persentase", f"{positive_rate:.2f}%")

    fig = px.pie(df, names=target_col, title="Distribusi Target")
    st.plotly_chart(fig, use_container_width=True)
