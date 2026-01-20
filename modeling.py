import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from catboost import CatBoostClassifier


def modeling_page():

    # =========================
    # PENGAMAN STATE
    # =========================
    required_keys = ["df", "target_col", "dataset_type"]
    for key in required_keys:
        if key not in st.session_state:
            st.warning("Silakan upload dataset terlebih dahulu.")
            return

    df = st.session_state["df"]
    target_col = st.session_state["target_col"]
    dataset_type = st.session_state["dataset_type"]

    # =========================
    # VALIDASI TARGET
    # =========================
    if target_col not in df.columns:
        st.error("❌ Target kolom tidak ditemukan pada dataset.")
        st.write("Kolom tersedia:", list(df.columns))
        st.write("Target yang dicari:", target_col)
        st.stop()

    # =========================
    # HEADER
    # =========================
    st.subheader("Machine Learning")
    st.write(f"Jenis Dataset: **{dataset_type}**")
    st.write(f"Target Klasifikasi: **{target_col}**")
    st.markdown("---")

    # =========================
    # PREPROCESSING
    # =========================
    df_model = df.copy()

    for col in df_model.columns:
        df_model[col] = pd.to_numeric(df_model[col], errors="coerce")

    before = len(df_model)
    df_model = df_model.dropna()
    after = len(df_model)

    st.info(f"Data dibersihkan: {before - after} baris dibuang")

    # =========================
    # SPLIT FITUR & TARGET
    # =========================
    X = df_model.drop(columns=[target_col], errors="ignore")
    y = df_model[target_col]

    if X.empty:
        st.error("❌ Tidak ada fitur setelah preprocessing.")
        st.stop()

    # =========================
    # TRAIN TEST SPLIT
    # =========================
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # =========================
    # SCALING
    # =========================
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    st.session_state["scaler"] = scaler
    st.session_state["feature_columns"] = X.columns.tolist()

    # =========================
    # MODEL DEFINISI
    # =========================
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "SVM": SVC(probability=True, random_state=42),
        "CatBoost": CatBoostClassifier(
            iterations=200,
            learning_rate=0.1,
            depth=6,
            verbose=0,
            random_state=42
        )
    }

    results = []
    conf_matrices = {}

    best_model = None
    best_f1 = 0
    best_name = None

    # =========================
    # TRAINING & EVALUASI
    # =========================
    for name, model in models.items():

        if name in ["Logistic Regression", "SVM"]:
            model.fit(X_train_scaled, y_train)
            y_pred = model.predict(X_test_scaled)
        else:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, zero_division=0)
        rec = recall_score(y_test, y_pred, zero_division=0)
        f1 = f1_score(y_test, y_pred, zero_division=0)

        conf_matrices[name] = confusion_matrix(y_test, y_pred)

        results.append({
            "Algoritma": name,
            "Accuracy (%)": round(acc * 100, 2),
            "Precision (%)": round(prec * 100, 2),
            "Recall (%)": round(rec * 100, 2),
            "F1-Score (%)": round(f1 * 100, 2)
        })

        if f1 > best_f1:
            best_f1 = f1
            best_model = model
            best_name = name

    results_df = pd.DataFrame(results)

    # =========================
    # OUTPUT
    # =========================
    st.subheader("Hasil Evaluasi Model")
    st.dataframe(results_df, use_container_width=True)

    st.success(f"Model Terbaik: **{best_name}** (F1 = {best_f1:.4f})")

    st.subheader("Confusion Matrix")
    selected = st.selectbox("Pilih Model", list(conf_matrices.keys()))
    st.dataframe(conf_matrices[selected])

    st.session_state["best_model"] = best_model
