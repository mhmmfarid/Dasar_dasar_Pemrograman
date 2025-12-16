import streamlit as st

# Style 
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 60px;
        min-height: 100vh;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .title {
        color: #ffeaa7;
        font-size: 52px;
        text-align: center;
        font-weight: bold;
        text-shadow: 3px 3px 10px rgba(0,0,0,0.4);
        margin-bottom: 30px;
        animation: slideIn 2s ease-out;
    }
    .subtitle {
        color: #fd79a8;
        font-size: 24px;
        text-align: center;
        margin-bottom: 60px;
        font-weight: 500;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
        animation: fadeIn 2s ease-out 0.5s both;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.98);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        margin: 20px;
        transition: transform 0.5s ease, box-shadow 0.5s ease, background-color 0.3s ease;
        text-align: center;
        color: #2d3436;
        border: 2px solid rgba(255,255,255,0.3);
        position: relative;
        overflow: hidden;
    }
    .card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: left 0.5s;
    }
    .card:hover::before {
        left: 100%;
    }
    .card:hover {
        transform: scale(1.08);
        box-shadow: 0 15px 30px rgba(0,0,0,0.3);
        background-color: rgba(255, 255, 255, 1);
    }
    .card h3 {
        color: #00b894;
        margin-bottom: 20px;
        font-size: 26px;
        font-weight: 600;
    }
    .card p {
        color: #636e72;
        font-size: 18px;
        line-height: 1.6;
    }
    .btn {
        background: linear-gradient(45deg, #6c5ce7, #a29bfe);
        color: white;
        padding: 15px 30px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        font-size: 18px;
        margin-top: 25px;
        transition: all 0.4s ease;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .btn:hover {
        background: linear-gradient(45deg, #5649c0, #8c7ae6);
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-100px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Header 
st.markdown('<div class="title">🧮 Selamat Datang di Kalkulator Sederhana</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Aplikasi kalkulator interaktif dengan fitur multi-page untuk kemudahan dan efisiensi Anda! 🎉</div>', unsafe_allow_html=True)

# Layout 
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><h3>🧮 Kalkulator Dasar</h3><p>Lakukan operasi matematika dasar seperti tambah, kurang, kali, bagi, dan pangkat dengan mudah dan cepat. 🚀</p></div>', unsafe_allow_html=True)
    if st.button("Mulai Hitung", key="kalkulator"):
        st.switch_page("pages/kalkulator.py")  

with col2:
    st.markdown('<div class="card"><h3>📜 Riwayat Perhitungan</h3><p>Lihat dan kelola riwayat kalkulasi Anda yang tersimpan selama sesi ini. 📊</p></div>', unsafe_allow_html=True)
    if st.button("Lihat Riwayat", key="riwayat"):
        st.switch_page("pages/riwayat.py")  
        

col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="card"><h3>ℹ️ Tentang</h3><p>Pelajari lebih lanjut tentang fitur, teknologi, dan cara kerja aplikasi ini. 💡</p></div>', unsafe_allow_html=True)
    if st.button("Pelajari Lebih", key="tentang"):
        st.switch_page("pages/tentang.py")  

with col4:
    st.markdown('<div class="card"><h3>🧭 Navigasi</h3><p>Gunakan sidebar untuk berpindah halaman dengan cepat dan intuitif. 🧭</p><p style="font-size:16px; color:#999;">Sidebar tersedia di sisi kiri layar.</p></div>', unsafe_allow_html=True)


st.write("---")
st.info("💡 Tip: Klik kartu untuk mulai eksplorasi aplikasi yang menyenangkan ini!")
