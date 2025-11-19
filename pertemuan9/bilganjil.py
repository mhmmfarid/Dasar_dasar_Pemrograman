def bilangan_ganjil(batas_atas):
  ganjil_list = []
  for i in range(1, batas_atas):
    if i % 2 != 0:
      ganjil_list.append(str(i))
  
  
  return ",".join(ganjil_list)
output_ganjil = bilangan_ganjil(20)
print(f"bilangan(20) #{output_ganjil}")