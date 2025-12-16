import streamlit as st

st.title("Tentang Aplikasi Kalkulator Sederhana")
st.write("Aplikasi ini adalah alat interaktif yang dirancang untuk memudahkan pengguna dalam melakukan perhitungan matematika dasar secara cepat dan akurat. Dibangun dengan Streamlit, aplikasi ini menawarkan pengalaman pengguna yang intuitif, tanpa perlu instalasi perangkat lunak tambahan, cukup akses melalui browser web.")

st.subheader("Fitur Utama:")
st.markdown("""
- **Operasi Matematika Dasar**: Mendukung penjumlahan, pengurangan, perkalian, pembagian, dan pemangkatan, memungkinkan pengguna menyelesaikan tugas sehari-hari seperti perhitungan keuangan atau akademik dengan mudah.
- **Riwayat Kalkulasi Tersimpan**: Setiap perhitungan otomatis disimpan dalam sesi, sehingga pengguna dapat melacak dan mereview hasil sebelumnya tanpa khawatir kehilangan data.
- **Penanganan Error Cerdas**: Sistem validasi otomatis mencegah kesalahan seperti pembagian oleh nol, memberikan pesan error yang jelas untuk memandu pengguna.
- **Navigasi Multi-Halaman**: Antarmuka dengan beberapa halaman (landing page, kalkulator, riwayat, dan tentang) untuk navigasi yang lancar dan terorganisir.
""")

st.subheader("Teknologi yang Digunakan:")
st.write("- **Streamlit**: Framework Python untuk membangun aplikasi web interaktif dengan cepat, fokus pada UI yang responsif dan mudah digunakan.")
st.write("- **Python**: Bahasa pemrograman utama, dengan implementasi logika if untuk validasi, looping untuk menampilkan riwayat, functions untuk operasi matematika, dan modul math untuk perhitungan lanjutan seperti pangkat.")
st.write("Teknologi ini dipilih untuk memastikan aplikasi ringan, aman, dan dapat diakses di berbagai perangkat.")

st.subheader("Cara Kerja Aplikasi:")
st.markdown("""
- **Input dan Operasi**: Pengguna memasukkan angka dan memilih operasi melalui antarmuka sederhana.
- **Perhitungan Real-Time**: Hasil dihitung instan menggunakan fungsi Python yang efisien.
- **Penyimpanan Sesi**: Riwayat disimpan sementara selama sesi browser untuk kemudahan akses.
- **Navigasi**: Klik tombol di landing page untuk pindah halaman, atau gunakan sidebar untuk eksplorasi.
""")

st.subheader("Pengembang:")
st.write("Dibuat oleh Kelompok 2 sebagai proyek pembelajaran dalam pengembangan aplikasi web dengan Python. Aplikasi ini bertujuan untuk mendemonstrasikan konsep dasar pemrograman seperti logika, fungsi, dan modul dalam konteks praktis.")
