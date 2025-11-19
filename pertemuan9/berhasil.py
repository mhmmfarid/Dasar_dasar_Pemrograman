def nilai(angka):
  # Mengembalikan 'lulus' jika nilai >= 70, dan 'gagal' jika < 70.
  if angka >= 70: # Batas kelulusan diasumsikan 70
    return "lulus"
  else:
    return "gagal"
print(f"nilai(80) #{nilai(80)}")
print(f"nilai(60) #{nilai(60)}") # Menggunakan 60 untuk menghasilkan 'gagal'