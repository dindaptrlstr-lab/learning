# Machine Learning Classification with Streamlit

## Deskripsi Proyek
Proyek ini merupakan aplikasi Machine Learning berbasis web menggunakan Streamlit
yang bertujuan untuk melakukan analisis data dan klasifikasi menggunakan beberapa
algoritma Machine Learning. Aplikasi ini menampilkan dashboard eksplorasi data,
proses pemodelan, evaluasi model, serta fitur prediksi berbasis input pengguna.

Proyek ini dibuat sebagai bagian dari pembelajaran mata kuliah Machine Learning
pada Program Studi Sains Data.

---

## Tujuan Proyek
Tujuan dari proyek ini adalah:
1. Menerapkan konsep Machine Learning klasifikasi pada data kesehatan dan lingkungan
2. Membandingkan performa beberapa algoritma Machine Learning
3. Menyajikan hasil analisis dan prediksi dalam bentuk aplikasi interaktif berbasis Streamlit
4. Melatih pemahaman end-to-end pipeline Machine Learning mulai dari data hingga deployment sederhana

---

## Dataset yang Digunakan
Proyek ini menggunakan dua dataset utama:
1. **Cardio Train Dataset**  
   Dataset kesehatan yang berisi data pasien untuk prediksi risiko penyakit kardiovaskular.

2. **Water Potability Dataset**  
   Dataset lingkungan yang digunakan untuk menentukan apakah air layak minum atau tidak
   berdasarkan parameter kimia dan fisika air.

Dataset disimpan dalam format `.csv` dan diproses sebelum digunakan dalam pemodelan.

---

## Algoritma Machine Learning
Algoritma yang digunakan dalam proyek ini meliputi:
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)
- CatBoost Classifier

Model dievaluasi menggunakan metrik evaluasi klasifikasi untuk menentukan performa terbaik.

---

## Fitur Aplikasi
Aplikasi Streamlit memiliki beberapa fitur utama:
- Dashboard eksplorasi data (EDA)
- Visualisasi distribusi data
- Training dan evaluasi model Machine Learning
- Perbandingan performa model
- Prediksi data baru berdasarkan input pengguna

---

## Tools & Library
Tools dan library yang digunakan dalam proyek ini:
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- CatBoost

Seluruh dependensi tercantum dalam file `requirements.txt`.

---

## Cara Menjalankan Aplikasi
Ikuti langkah-langkah berikut untuk menjalankan aplikasi secara lokal:

1. Clone repository ini:
   ```bash
   git clone https://github.com/dindaptrlstr-lab/learning.git
