import streamlit as st
import os
import random

# ======================================================
# PATH DASAR
# ======================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")

# ======================================================
# LOAD GAMBAR AMAN (SUPPORT SPASI & JPEG)
# ======================================================
def get_image_path(filename):
    for ext in ["jpg", "jpeg", "png"]:
        path = os.path.join(IMAGE_DIR, f"{filename}.{ext}")
        if os.path.exists(path):
            return path
    return None

# ======================================================
# KONFIGURASI HALAMAN
# ======================================================
st.set_page_config(
    page_title="Outfit Assistant 💖",
    page_icon="👗",
    layout="wide"
)

# ======================================================
# CSS UI (HALUS & ESTETIK)
# ======================================================
st.markdown("""
<style>
.main {
    background-color: #FFF0F5;
    font-family: 'Poppins', sans-serif;
}

h1, h2, h3 {
    color: #FF1493;
    text-align: center;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 24px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    max-width: 540px;
    margin: 0 auto 30px auto;
}

.soft-img img {
    border-radius: 22px;
    max-width: 420px;
    display: block;
    margin: auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

.badge {
    background: #FF69B4;
    color: white;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 14px;
    display: inline-block;
}

.stButton>button {
    background-color: #FF69B4;
    color: white;
    border-radius: 25px;
    padding: 10px 25px;
    font-size: 16px;
}

.stButton>button:hover {
    background-color: #FF1493;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# DATA (SESUAI ASSET KAMU)
# ======================================================
outfit_acara = {
    "Kerja Kantor": ("Outfit kerja rapi dan profesional", "1ke1"),
    "Hangout": ("Outfit santai untuk hangout", "hangout"),
    "Kencan": ("Outfit feminin untuk kencan", "kencan"),
    "Olahraga": ("Outfit nyaman untuk olahraga", "olahraga"),
    "Formal": ("Outfit resmi acara formal", "formal")
}

outfit_cuaca = {
    "Cerah": ("Outfit ringan untuk cuaca cerah", "cuaca cerah"),
    "Dingin": ("Outfit hangat untuk cuaca dingin", "cuaca dingin"),
    "Hujan": ("Outfit aman saat hujan", "hujan")
}

warna_outfit = {
    "Merah": ("Kombinasi merah elegan", "merah"),
    "Kuning": ("Kombinasi kuning ceria", "kuning"),
    "Hijau": ("Kombinasi hijau natural", "hijau"),
    "Pink": ("Kombinasi pink feminin", "pink"),
    "Biru": ("Kombinasi biru calm", "biru"),
    "Hitam": ("Kombinasi hitam classy", "hitam")
}

# ======================================================
# PAGE 1 — HALAMAN UTAMA (INTERAKTIF)
# ======================================================
def page_home():
    st.title("👗 Outfit Assistant")
    st.markdown("<p style='text-align:center;'>Temukan inspirasi outfit sesuai kebutuhanmu hari ini 💖</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<span class='badge'>🔥 Populer</span>", unsafe_allow_html=True)
        st.subheader("Outfit Acara")
        st.write("Cari outfit berdasarkan acara")
        if st.button("Buka Outfit Acara"):
            st.session_state.page = "acara"
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<span class='badge'>🌤 Cuaca</span>", unsafe_allow_html=True)
        st.subheader("Outfit Cuaca")
        st.write("Sesuaikan dengan cuaca hari ini")
        if st.button("Buka Outfit Cuaca"):
            st.session_state.page = "cuaca"
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<span class='badge'>🎨 Warna</span>", unsafe_allow_html=True)
        st.subheader("Kombinasi Warna")
        st.write("Padukan warna outfitmu")
        if st.button("Buka Kombinasi Warna"):
            st.session_state.page = "warna"
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("✨ Rekomendasi Acak Hari Ini")

    key = random.choice(list(outfit_acara.keys()))
    desc, img = outfit_acara[key]
    path = get_image_path(img)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader(key)
    if path:
        st.markdown("<div class='soft-img'>", unsafe_allow_html=True)
        st.image(path)
        st.markdown("</div>", unsafe_allow_html=True)
    st.success(desc)
    st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# PAGE 2 — OUTFIT ACARA
# ======================================================
def page_acara():
    st.title("📌 Outfit Berdasarkan Acara")
    pilihan = st.selectbox("Pilih acara", outfit_acara.keys())

    if st.button("✨ Tampilkan Outfit"):
        desc, img = outfit_acara[pilihan]
        path = get_image_path(img)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        if path:
            st.markdown("<div class='soft-img'>", unsafe_allow_html=True)
            st.image(path)
            st.markdown("</div>", unsafe_allow_html=True)
        st.success(desc)
        st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# PAGE 3 — OUTFIT CUACA
# ======================================================
def page_cuaca():
    st.title("🌤 Outfit Berdasarkan Cuaca")
    pilihan = st.selectbox("Pilih cuaca", outfit_cuaca.keys())

    if st.button("☁ Lihat Outfit"):
        desc, img = outfit_cuaca[pilihan]
        path = get_image_path(img)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        if path:
            st.markdown("<div class='soft-img'>", unsafe_allow_html=True)
            st.image(path)
            st.markdown("</div>", unsafe_allow_html=True)
        st.success(desc)
        st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# PAGE 4 — WARNA OUTFIT
# ======================================================
def page_warna():
    st.title("🎨 Kombinasi Warna Outfit")
    pilihan = st.selectbox("Pilih warna", warna_outfit.keys())

    if st.button("🎨 Tampilkan Kombinasi"):
        desc, img = warna_outfit[pilihan]
        path = get_image_path(img)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        if path:
            st.markdown("<div class='soft-img'>", unsafe_allow_html=True)
            st.image(path)
            st.markdown("</div>", unsafe_allow_html=True)
        st.success(desc)
        st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# SIDEBAR MULTI PAGE (4 PAGE)
# ======================================================
if "page" not in st.session_state:
    st.session_state.page = "home"

st.sidebar.title("👗 Outfit Assistant")

menu = st.sidebar.radio(
    "Navigasi",
    [
        "🏠 Beranda",
        "📌 Outfit Acara",
        "🌤 Outfit Cuaca",
        "🎨 Warna Outfit"
    ]
)

if menu == "🏠 Beranda":
    st.session_state.page = "home"
elif menu == "📌 Outfit Acara":
    st.session_state.page = "acara"
elif menu == "🌤 Outfit Cuaca":
    st.session_state.page = "cuaca"
elif menu == "🎨 Warna Outfit":
    st.session_state.page = "warna"

# ======================================================
# ROUTING PAGE
# ======================================================
if st.session_state.page == "home":
    page_home()
elif st.session_state.page == "acara":
    page_acara()
elif st.session_state.page == "cuaca":
    page_cuaca()
elif st.session_state.page == "warna":
    page_warna()

st.sidebar.markdown("---")
st.sidebar.markdown("💖 Kelompok 20")
