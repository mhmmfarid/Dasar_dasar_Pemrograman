import streamlit as st

# Style
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #6c5ce7 0%, #a29bfe 100%);
        padding: 50px;
        min-height: 100vh;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #ffeaa7;
        font-size: 48px;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        animation: slideIn 1.5s ease-out;
    }
    .subtitle {
        color: #fd79a8;
        font-size: 22px;
        text-align: center;
        margin-bottom: 50px;
        font-weight: 500;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.3);
        animation: slideIn 1.5s ease-out 0.3s both;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        margin: 15px;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        text-align: center;
        color: #2d3436;
        border: 1px solid rgba(255,255,255,0.2);
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0,0,0,0.25);
    }
    .card h3 {
        color: #6c5ce7;
        margin-bottom: 15px;
        font-size: 24px;
    }
    .card p {
        color: #636e72;
        font-size: 16px;
        line-height: 1.5;
    }
    .btn {
        background-color: #6c5ce7;
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 16px;
        margin-top: 20px;
        transition: background-color 0.3s ease, transform 0.2s ease;
        font-weight: bold;
    }
    .btn:hover {
        background-color: #5649c0;
        transform: translateY(-2px);
    }
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    </style>
""", unsafe_allow_html=True)

# Header1
st.markdown('<div class="title">🧮 Selamat Datang di Kalkulator Sederhana</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Aplikasi kalkulator interaktif dengan fitur multi-page untuk kemudahan dan efisiensi Anda</div>', unsafe_allow_html=True)

# Layout/container
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><h3>🧮 Kalkulator Dasar</h3><p>Lakukan operasi matematika dasar seperti tambah, kurang, kali, bagi, dan pangkat dengan mudah dan cepat.</p></div>', unsafe_allow_html=True)
    if st.button("Mulai Hitung", key="kalkulator"):
        st.switch_page("pages/kalkulator.py")  

with col2:
    st.markdown('<div class="card"><h3>📜 Riwayat Perhitungan</h3><p>Lihat dan kelola riwayat kalkulasi Anda yang tersimpan selama sesi ini.</p></div>', unsafe_allow_html=True)
    if st.button("Lihat Riwayat", key="riwayat"):
        st.switch_page("pages/riwayat.py")  

col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="card"><h3>ℹ️ Tentang</h3><p>Pelajari lebih lanjut tentang fitur, teknologi, dan cara kerja aplikasi ini.</p></div>', unsafe_allow_html=True)
    if st.button("Pelajari Lebih", key="tentang"):
        st.switch_page("pages/tentang.py")  

with col4:
    st.markdown('<div class="card"><h3>🧭 Navbar</h3><p>Gunakan sidebar untuk berpindah halaman dengan cepat dan intuitif.</p><p style="font-size:14px; color:#999;">Sidebar tersedia di sisi kiri layar.</p></div>', unsafe_allow_html=True)
   