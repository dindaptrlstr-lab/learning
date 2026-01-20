Machine Learning Classification with Streamlit
Latar Belakang

Perkembangan Machine Learning memungkinkan pemanfaatan data dalam berbagai bidang,
termasuk kesehatan dan lingkungan, untuk mendukung pengambilan keputusan berbasis data.
Metode klasifikasi digunakan secara luas untuk memprediksi suatu kondisi atau kategori
berdasarkan karakteristik numerik tertentu.

Proyek ini dikembangkan sebagai implementasi praktis dari konsep Machine Learning
klasifikasi, mulai dari tahap eksplorasi data, pemodelan, evaluasi, hingga deployment
sederhana dalam bentuk aplikasi web interaktif menggunakan Streamlit.
Proyek ini juga bertujuan untuk melatih pemahaman end-to-end pipeline Machine Learning
sesuai dengan capaian pembelajaran mata kuliah Machine Learning pada Program Studi Sains Data.

Tujuan Proyek

Tujuan dari pengembangan proyek ini adalah:

Menerapkan algoritma Machine Learning klasifikasi pada data kesehatan dan lingkungan

Melakukan eksplorasi data (Exploratory Data Analysis/EDA) untuk memahami karakteristik dataset

Membandingkan performa beberapa algoritma klasifikasi berdasarkan metrik evaluasi

Menyajikan hasil analisis dan prediksi dalam bentuk aplikasi web interaktif berbasis Streamlit

Mengimplementasikan alur kerja Machine Learning secara menyeluruh, mulai dari preprocessing data hingga deployment

Dataset yang Digunakan

Proyek ini menggunakan dua dataset utama dalam format .csv, yaitu:

Cardio Train Dataset
Dataset bidang kesehatan yang berisi data pasien, seperti usia, tekanan darah,
kadar kolesterol, dan indikator lainnya, yang digunakan untuk memprediksi risiko
penyakit kardiovaskular.

Water Potability Dataset
Dataset bidang lingkungan yang digunakan untuk menentukan kelayakan air minum
berdasarkan parameter fisik dan kimia air, seperti pH, hardness, solids, dan
kandungan zat lainnya.

Sebelum digunakan dalam pemodelan, dataset melalui tahap preprocessing yang meliputi
penanganan missing value, normalisasi data, serta pembagian data menjadi data latih
dan data uji.

Metode dan Algoritma Machine Learning

Metode yang digunakan dalam proyek ini adalah klasifikasi supervised learning.
Beberapa algoritma Machine Learning yang diterapkan dan dibandingkan performanya antara lain:

Logistic Regression

Decision Tree Classifier

Random Forest Classifier

Support Vector Machine (SVM)

CatBoost Classifier

Evaluasi model dilakukan menggunakan metrik evaluasi klasifikasi seperti akurasi,
confusion matrix, serta precision, recall, dan F1-score untuk menentukan model dengan
performa terbaik. Model terbaik selanjutnya digunakan pada fitur prediksi.

Fitur Aplikasi

Aplikasi yang dibangun menggunakan Streamlit memiliki fitur-fitur utama sebagai berikut:

Dashboard eksplorasi data (Exploratory Data Analysis)

Visualisasi distribusi dan karakteristik data

Proses training dan evaluasi beberapa model Machine Learning

Perbandingan performa antar model klasifikasi

Prediksi data baru berdasarkan input pengguna menggunakan model terbaik

Tools dan Library

Tools dan library yang digunakan dalam pengembangan proyek ini meliputi:

Python

Streamlit

Pandas

NumPy

Scikit-learn

Plotly

CatBoost

Seluruh dependensi proyek telah dicantumkan dalam file requirements.txt.

Cara Menjalankan Aplikasi

Untuk menjalankan aplikasi secara lokal, ikuti langkah-langkah berikut:

Clone repository:

git clone https://github.com/dindaptrlstr-lab/learning.git


Masuk ke direktori proyek:

cd learning


Install seluruh dependensi:

pip install -r requirements.txt


Jalankan aplikasi Streamlit:

streamlit run app.py


Aplikasi akan berjalan dan dapat diakses melalui browser pada alamat:

http://localhost:8501

Catatan

Proyek ini dikembangkan untuk keperluan akademik dan pembelajaran Machine Learning.
Hasil prediksi yang dihasilkan oleh aplikasi tidak dimaksudkan sebagai diagnosis
atau keputusan final, melainkan sebagai simulasi penerapan metode klasifikasi
berbasis data.
