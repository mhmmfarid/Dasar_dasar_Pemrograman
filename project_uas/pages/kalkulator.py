import streamlit as st
import math  # Module untuk operasi matematika dan trigonometri

# Functions Aritmatika
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:  #  if untuk validasi
        return a / b
    else:
        return "Error"

def power(a, b):
    return math.pow(a, b)  #module math

# Functions Trigonometri (Bangun Datar)
def luas_persegi(sisi):
    return sisi ** 2

def keliling_persegi(sisi):
    return 4 * sisi

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

def keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

# Functions
def luas_permukaan_kubus(sisi):
    return 6 * sisi ** 2

def volume_kubus(sisi):
    return sisi ** 3

def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

st.title("🧮 Kalkulator Gabungan")
st.write("Pilih program kalkulator yang ingin dijalankan.")

# Selectbox pilih program
program = st.selectbox("Pilih Program", ["Kalkulator Aritmatika", "Kalkulator Trigonometri"])

result = None
calculation_detail = ""  # riwayat

if program == "Kalkulator Aritmatika":
    st.subheader("Kalkulator Aritmatika")
    st.write("Masukkan angka dan pilih operasi.")
    
    num1 = st.number_input("Angka pertama", value=0, step=0)
    num2 = st.number_input("Angka kedua", value=0, step=0)
    operation = st.selectbox("Operasi", ["+", "-", "*", "/", "**"])
    
    if operation == "+":
        result = add(num1, num2)
        calculation_detail = f"{num1} + {num2}"
    elif operation == "-":
        result = subtract(num1, num2)
        calculation_detail = f"{num1} - {num2}"
    elif operation == "*":
        result = multiply(num1, num2)
        calculation_detail = f"{num1} * {num2}"
    elif operation == "/":
        result = divide(num1, num2)
        calculation_detail = f"{num1} / {num2}"
    elif operation == "**":
        result = power(num1, num2)
        calculation_detail = f"{num1} ** {num2}"
    
    if st.button("Hitung"):
        if result is not None:
            st.success(f"Hasil: {result}")
            # Simpan riwayat
            if 'history' not in st.session_state:
                st.session_state.history = []
            st.session_state.history.append(f"Aritmatika: {calculation_detail} = {result}")
        else:
            st.error("Pilih operasi yang valid.")

elif program == "Kalkulator Trigonometri":
    st.subheader("Kalkulator Trigonometri")
    st.write("Pilih jenis bangun dan perhitungan.")
    
    jenis_bangun = st.selectbox("Pilih Jenis Bangun", ["Bangun Datar", "Bangun Ruang"])
    
    if jenis_bangun == "Bangun Datar":
        bangun_datar = st.selectbox("Pilih Bangun Datar", ["Persegi", "Segitiga", "Lingkaran"])
        perhitungan = st.selectbox("Pilih Perhitungan", ["Luas", "Keliling"])
        
        if bangun_datar == "Persegi":
            sisi = st.number_input("Panjang Sisi", value=0, step=0, min_value=0)
            if perhitungan == "Luas" and st.button("Hitung Luas Persegi"):
                if sisi < 0:
                    st.error("Nilai sisi tidak boleh negatif.")
                    result = None
                else:
                    result = luas_persegi(sisi)
                    calculation_detail = f"Luas Persegi: sisi={sisi}"
            elif perhitungan == "Keliling" and st.button("Hitung Keliling Persegi"):
                if sisi < 0:
                    st.error("Nilai sisi tidak boleh negatif.")
                    result = None
                else:
                    result = keliling_persegi(sisi)
                    calculation_detail = f"Keliling Persegi: sisi={sisi}"
        
        elif bangun_datar == "Segitiga":
            if perhitungan == "Luas":
                alas = st.number_input("Alas", value=0, step=0, min_value=0)
                tinggi = st.number_input("Tinggi", value=0, step=0, min_value=0)
                if st.button("Hitung Luas Segitiga"):
                    if alas < 0 or tinggi < 0:
                        st.error("Nilai alas dan tinggi tidak boleh negatif.")
                        result = None
                    else:
                        result = luas_segitiga(alas, tinggi)
                        calculation_detail = f"Luas Segitiga: alas={alas}, tinggi={tinggi}"
            elif perhitungan == "Keliling":
                sisi1 = st.number_input("Sisi 1", value=0, step=0, min_value=0)
                sisi2 = st.number_input("Sisi 2", value=0, step=0, min_value=0)
                sisi3 = st.number_input("Sisi 3", value=0, step=0, min_value=0)
                if st.button("Hitung Keliling Segitiga"):
                    if sisi1 < 0 or sisi2 < 0 or sisi3 < 0:
                        st.error("Nilai sisi tidak boleh negatif.")
                        result = None
                    else:
                        result = keliling_segitiga(sisi1, sisi2, sisi3)
                        calculation_detail = f"Keliling Segitiga: sisi1={sisi1}, sisi2={sisi2}, sisi3={sisi3}"
        
        elif bangun_datar == "Lingkaran":
            jari_jari = st.number_input("Jari-Jari", value=0, step=0, min_value=0)
            if perhitungan == "Luas" and st.button("Hitung Luas Lingkaran"):
                if jari_jari < 0:
                    st.error("Nilai jari-jari tidak boleh negatif.")
                    result = None
                else:
                    result = luas_lingkaran(jari_jari)
                    calculation_detail = f"Luas Lingkaran: jari_jari={jari_jari}"
            elif perhitungan == "Keliling" and st.button("Hitung Keliling Lingkaran"):
                if jari_jari < 0:
                    st.error("Nilai jari-jari tidak boleh negatif.")
                    result = None
                else:
                    result = keliling_lingkaran(jari_jari)
                    calculation_detail = f"Keliling Lingkaran: jari_jari={jari_jari}"
    
    elif jenis_bangun == "Bangun Ruang":
        bangun_ruang = st.selectbox("Pilih Bangun Ruang", ["Kubus", "Balok"])
        perhitungan = st.selectbox("Pilih Perhitungan", ["Luas Permukaan", "Volume"])
        
        if bangun_ruang == "Kubus":
            sisi = st.number_input("Panjang Sisi", value=0, step=0, min_value=0)
            if perhitungan == "Luas Permukaan" and st.button("Hitung Luas Permukaan Kubus"):
                if sisi < 0:
                    st.error("Nilai sisi tidak boleh negatif.")
                    result = None
                else:
                    result = luas_permukaan_kubus(sisi)
                    calculation_detail = f"Luas Permukaan Kubus: sisi={sisi}"
            elif perhitungan == "Volume" and st.button("Hitung Volume Kubus"):
                if sisi < 0:
                    st.error("Nilai sisi tidak boleh negatif.")
                    result = None
                else:
                    result = volume_kubus(sisi)
                    calculation_detail = f"Volume Kubus: sisi={sisi}"
        
        elif bangun_ruang == "Balok":
            panjang = st.number_input("Panjang", value=0, step=0, min_value=0)
            lebar = st.number_input("Lebar", value=0, step=0, min_value=0)
            tinggi = st.number_input("Tinggi", value=0, step=0, min_value=0)
            if perhitungan == "Luas Permukaan" and st.button("Hitung Luas Permukaan Balok"):
                if panjang < 0 or lebar < 0 or tinggi < 0:
                    st.error("Nilai panjang, lebar, dan tinggi tidak boleh negatif.")
                    result = None
                else:
                    result = luas_permukaan_balok(panjang, lebar, tinggi)
                    calculation_detail = f"Luas Permukaan Balok: panjang={panjang}, lebar={lebar}, tinggi={tinggi}"
            elif perhitungan == "Volume" and st.button("Hitung Volume Balok"):
                if panjang < 0 or lebar < 0 or tinggi < 0:
                    st.error("Nilai panjang, lebar, dan tinggi tidak boleh negatif.")
                    result = None
                else:
                    result = volume_balok(panjang, lebar, tinggi)
                    calculation_detail = f"Volume Balok: panjang={panjang}, lebar={lebar}, tinggi={tinggi}"
    
    # Tampilan hasil untuk trigonometri
    if result is not None:
        st.success(f"Hasil: {result:.2f}")
        # Simpan riwayat
        if 'history' not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append(f"Trigonometri: {calculation_detail} = {result:.2f}")

st.write("---")
st.info("Riwayat perhitungan tersimpan dan bisa dilihat di halaman Riwayat.")
