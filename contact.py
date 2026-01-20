import streamlit as st


def contact_page():

    # =========================
    # STYLE CONTACT PAGE
    # =========================
    st.markdown("""
    <style>
    .contact-card {
        background-color: #E7BEF8; /* Soft Lilac */
        padding: 32px;
        border-radius: 20px;
        max-width: 720px;
        margin: auto;
    }

    .contact-title {
        color: #F2619C; /* Raspberry Rose */
        font-weight: 700;
        text-align: center;
        margin-bottom: 12px;
    }

    .contact-text {
        font-size: 16px;
        color: #2E2E2E;
        line-height: 1.8;
        text-align: center;
    }

    .contact-link {
        color: #93ABD9; /* Blueberry Milk */
        font-weight: 600;
        text-decoration: none;
    }

    .contact-link:hover {
        text-decoration: underline;
    }

    /* Info box */
    div[data-testid="stAlert"] {
        background-color: #EDE986 !important; /* Lemon Cream */
        color: #2E2E2E !important;
        border-radius: 16px;
        border: none;
        max-width: 720px;
        margin: 24px auto;
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # HEADER
    # =========================
    st.markdown(
        "<h2 class='contact-title'>Contact</h2>",
        unsafe_allow_html=True
    )

    # =========================
    # CONTACT CARD
    # =========================
    st.markdown("""
    <div class="contact-card">
        <div class="contact-text">
            <strong>Nama Mahasiswa</strong><br>
            Dinda Putri Lestari<br><br>

            <strong>Program Studi</strong><br>
            S1 Sains Data<br><br>

            <strong>Universitas</strong><br>
            Universitas Muhammadiyah Semarang<br><br>

            📧 <strong>Email</strong><br>
            dindaptrlstr@gmail.com<br><br>

            🔗 <strong>GitHub</strong><br>
            <a class="contact-link" href="https://github.com/dindaptrlstr-lab" target="_blank">
                github.com/dindaptrlstr-lab
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # FOOTNOTE
    # =========================
    st.info(
        "Halaman ini berisi informasi identitas penyusun "
        "sebagai bagian dari **Proyek Akhir UAS Mata Kuliah Machine Learning**."
    )
