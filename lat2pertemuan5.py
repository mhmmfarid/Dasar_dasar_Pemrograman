pilihan = input("""
Silahkan pilih menu yang di inginkan
====================================
1. Luas Persegi
2. Luas Lingkaran
3. Luas Segitiga
====================================
Kirimkan hanya angka saja,
jawaban = """)

print(type(pilihan))
match pilihan:
  case "1":
    sisi = int(input("sisi = "))
    luas = sisi * sisi

    print(f"luas persegi dengan sisi {sisi} adalah {luas}")
    # luas persegi
  case "2":    
    # luas lingkaran
    # phi * jarjjari**2
    jarijari = int(input("jarijari = "))
    luas = 3.14 * jarijari**2

    print(f"luas lingkaran dengan jarijari {jarijari} adalah {luas}")
    
    print( "")
  case "3":
    # luas segitiga
    # (alas * tinggi)/2
    
    alas = float(input("masukan alas segitiga = "))
    tinggi = float(input("masukan tinggi segitiga = "))
    
    luassegitiga = 0.5 * alas * tinggi
    print ("luas segitiga", luassegitiga)

  
  
  
  case _:
    print("yaa")