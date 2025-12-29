import streamlit as st
import os
from utils import calculate_risk, risk_category

# =======================
# PAGE CONFIG
# =======================
st.set_page_config(
    page_title="Cek Risiko Diabetes",
    page_icon="🩺",
    layout="wide"
)

# =======================
# BASE DIRECTORY (AMAN UNTUK DEPLOY)
# =======================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "assets", "img1.jpg")

# =======================
# GLOBAL STYLE
# =======================
st.markdown("""
<style>
.stApp {
    background-color: #f8f9fa;
}

.feature-card {
    background-color: #d3d3d3;
    padding: 30px 20px;
    border-radius: 12px;
    text-align: center;
    font-weight: 600;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    cursor: pointer;
}

.feature-card:hover {
    transform: translateY(-10px) scale(1.05);
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    background-color: #8e9bad;
}
</style>
""", unsafe_allow_html=True)

# =======================
# SIDEBAR
# =======================
st.sidebar.title("🩺 Cek Risiko Diabetes")
page = st.sidebar.selectbox(
    "Pilih Halaman",
    ["Home", "Input Data", "Kalkulasi Risiko", "Hasil"]
)

# =======================
# SESSION STATE
# =======================
if "user_data" not in st.session_state:
    st.session_state.user_data = {}

if "risk_score" not in st.session_state:
    st.session_state.risk_score = None

# =======================
# HOME PAGE
# =======================
if page == "Home":
    st.title("🩺 Aplikasi Cek Risiko Diabetes")

    st.write(
        "Aplikasi ini membantu mengevaluasi risiko diabetes berdasarkan "
        "usia, BMI, aktivitas fisik, dan riwayat keluarga."
    )

    st.divider()
    st.subheader("✨ Fitur Utama Aplikasi")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            📝<br><br>
            Input Data Sederhana
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            📊<br><br>
            Kalkulasi Risiko
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            💡<br><br>
            Saran Pencegahan
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ===== IMAGE (AMAN SAAT DEPLOY)
    if os.path.exists(IMAGE_PATH):
        st.image(
            IMAGE_PATH,
            caption="Cegah diabetes sejak dini",
            use_container_width=True
        )
    else:
        st.warning("Gambar tidak ditemukan. Pastikan folder assets ada di GitHub.")

# =======================
# INPUT DATA PAGE
# =======================
elif page == "Input Data":
    st.title("📝 Input Data Pengguna")

    with st.form("form_input"):
        age = st.number_input("Usia (tahun)", min_value=1, max_value=120, step=1)
        weight = st.number_input("Berat badan (kg)", min_value=1.0)
        height = st.number_input("Tinggi badan (cm)", min_value=50.0)
        family_history = st.selectbox("Riwayat keluarga diabetes", ["Tidak", "Ya"])
        activity_level = st.selectbox(
            "Aktivitas fisik",
            ["Rendah", "Sedang", "Tinggi"]
        )

        submit = st.form_submit_button("Simpan Data")

    if submit:
        st.session_state.user_data = {
            "age": age,
            "weight": weight,
            "height": height,
            "family_history": family_history,
            "activity_level": activity_level
        }
        st.success("Data berhasil disimpan.")

# =======================
# CALCULATION PAGE
# =======================
elif page == "Kalkulasi Risiko":
    st.title("🔍 Kalkulasi Risiko Diabetes")

    if not st.session_state.user_data:
        st.warning("Isi data terlebih dahulu.")
    else:
        st.json(st.session_state.user_data)

        if st.button("Hitung Risiko"):
            score = calculate_risk(st.session_state.user_data)
            st.session_state.risk_score = score
            st.success("Perhitungan selesai.")

# =======================
# RESULT PAGE
# =======================
elif page == "Hasil":
    st.title("📊 Hasil Evaluasi Risiko Diabetes")

    if st.session_state.risk_score is None:
        st.warning("Lakukan perhitungan terlebih dahulu.")
    else:
        score = st.session_state.risk_score
        category = risk_category(score)

        st.metric("Skor Risiko", score)
        st.subheader(f"Tingkat Risiko: {category}")

        if category == "Rendah":
            st.success("Risiko rendah. Pertahankan gaya hidup sehat.")
        elif category == "Sedang":
            st.warning("Risiko sedang. Mulai perbaiki pola hidup.")
        else:
            st.error("Risiko tinggi. Disarankan konsultasi ke tenaga medis.")

        st.info(
            "⚠️ Skor ini hanya estimasi dan bukan diagnosis medis."
        )
