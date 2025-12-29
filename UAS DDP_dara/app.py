import streamlit as st
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
# GLOBAL STYLE (AMAN + HOVER)
# =======================
st.markdown("""
<style>
.stApp {
    background-color: #f8f9fa;
}

/* CARD ANIMATION */
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
# SIDEBAR NAVIGATION
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
        "data pribadi sederhana seperti usia, BMI, aktivitas fisik, dan "
        "riwayat keluarga."
    )

    st.divider()

    st.subheader("✨ Fitur Utama Aplikasi")

    # ===== 3 FEATURE CARDS (ANIMASI HOVER)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            📝<br><br>
            Yuk! Input Data Sederhana
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            📊<br><br>
            Lalu, Kalkulasi Risikonya
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            💡<br><br>
            Dan Cek Saran Pencegahan
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ===== IMAGE
    st.image(
        "assets/img1.jpg",
        caption="Cegah diabetes sejak dini",
        use_container_width=True
    )

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
        st.success("Data berhasil disimpan. Lanjut ke Kalkulasi Risiko.")

# =======================
# CALCULATION PAGE
# =======================
elif page == "Kalkulasi Risiko":
    st.title("🔍 Kalkulasi Risiko Diabetes")

    if not st.session_state.user_data:
        st.warning("Isi data terlebih dahulu di halaman Input Data.")
    else:
        st.subheader("Data Pengguna")
        st.json(st.session_state.user_data)

        if st.button("Hitung Risiko"):
            score = calculate_risk(st.session_state.user_data)
            st.session_state.risk_score = score
            st.success("Perhitungan selesai. Lihat hasil di halaman Hasil.")

# =======================
# RESULT PAGE
# =======================
elif page == "Hasil":
    st.title("📊 Hasil Evaluasi Risiko Diabetes")

    if st.session_state.risk_score is None:
        st.warning("Lakukan perhitungan risiko terlebih dahulu.")
    else:
        score = st.session_state.risk_score
        category = risk_category(score)

        st.metric("Skor Risiko", score)
        st.subheader(f"Tingkat Risiko: {category}")

        st.markdown("""
        **Interpretasi Skor Risiko:**
        - **Skor < 30** → Risiko diabetes **rendah**
        - **Skor 30 – 59** → Risiko diabetes **sedang**
        - **Skor ≥ 60** → Risiko diabetes **tinggi**
        """)

        if category == "Rendah":
            st.success(
                "Risiko Anda tergolong **rendah**. " 
                "Hal ini menunjukkan bahwa faktor risiko diabetes saat ini " 
                "masih minimal. Tetap pertahankan pola hidup sehat."
            )
        elif category == "Sedang":
            st.warning(
                "Risiko Anda berada pada tingkat **sedang**. " 
                "Disarankan untuk mulai memperbaiki pola makan, " 
                "meningkatkan aktivitas fisik, dan melakukan pemeriksaan " 
                "kesehatan secara berkala."
            )
        else:
            st.error(
                "Risiko Anda tergolong **tinggi**. " 
                "Hal ini menunjukkan adanya faktor risiko yang signifikan. " 
                "Sangat disarankan untuk berkonsultasi dengan tenaga medis " 
                "atau dokter untuk pemeriksaan lebih lanjut."
            )

        st.info(
            "⚠️ **Catatan:** Skor ini bersifat *estimasi* berdasarkan data " 
            "yang dimasukkan dan **bukan diagnosis medis**. " 
            "Hasil ini digunakan sebagai sarana edukasi dan kesadaran " 
            "awal terhadap risiko diabetes."
        )