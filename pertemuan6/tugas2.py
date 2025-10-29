#Buat lah output dari menggunakan bahasa pemprograman 
#python dengan 
#1 + 3 + 5 + 7 +9 +11 +13 + 15 +17 +19 = ….

jumlah = 0 #Variable untuk menyimpan nilai
string = "" #Untuk membaca tanda +

bilangan = 1
while bilangan <= 19: #Untuk melakukan perulangan sebanyak 19×
 jumlah += bilangan
 string += str(bilangan)
 if bilangan < 19:
   string += '+'
 bilangan += 2
print(string, '=' ,jumlah)