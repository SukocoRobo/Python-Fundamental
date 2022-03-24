"""
This is python code for looping "Read book" dengan while
"""
jumlah_buku = 10
print('Perintah ibu,"Baca semua buku hingga paham"')
total_jumlah_baca = 0

jumlah_buku_dibaca_dan_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan di pahami {jumlah_buku_dibaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku *2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_dibaca_dan_dipahami == 9:
        print(f"buku ke {jumlah_buku_dibaca_dan_dipahami} belum pahami")
    else:
        jumlah_buku_dibaca_dan_dipahami = jumlah_buku_dibaca_dan_dipahami + 1
        print(f"buku ke {jumlah_buku_dibaca_dan_dipahami} sudah di baca dan dipahami")

if jumlah_buku_dibaca_dan_dipahami == jumlah_buku:
    print('Bu, Semua buku sudah dibaca dan di pahami')
else:
    print(f'tidak semua buku sudah di pahami.'
          f' anak hanya bisa memahami {jumlah_buku_dibaca_dan_dipahami}')
# print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_dibaca_dan_dipahami}')
