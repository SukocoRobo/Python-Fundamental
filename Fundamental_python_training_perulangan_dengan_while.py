"""
This is python code for looping "Read book" dengan while
"""
jumlah_buku = 10
print('Perintah ibu,"Baca semua buku hingga paham"')

jumlah_buku_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_buku_dibaca}')

while jumlah_buku_dibaca < jumlah_buku:
    print('Baca 1 buku yang belum dibaca')
    jumlah_buku_dibaca = jumlah_buku_dibaca + 1
    print(f"buku ke {jumlah_buku_dibaca} sudah di baca")


print(f'Jumlah buku yang sudah dibaca {jumlah_buku_dibaca}')
