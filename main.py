print("Menambah SSD")
SSD_awal = 256
SSD_tambahan = 256
SSD_sekarang = SSD_awal + SSD_tambahan

while True:
  try:
    SSD_awal = int(input("Masukkan SSD awal : "))
    SSD_tambahan = int(input("Masukkan jumlah SSD yang akan ditambah : "))
    SSD_sekarang = SSD_awal + SSD_tambahan
    break

  except ValueError:
    print("Yang anda input bukan angka")

print("Berhasil, SSD sekarang adalah : ")
print(SSD_awal,'+',SSD_tambahan,'=',SSD_sekarang)