"""
This is python code for looping "Read book" dengan while
"""
book_count = 10
print('Perintah ibu,"Baca semua buku hingga paham"')
read_book = 0

understood_count = 0
print(f'Jumlah buku yang sudah dibaca dan di pahami {understood_count}')

while read_book < book_count *2:
    read_book = read_book + 1
    if understood_count == 9:
        print(f"buku ke {understood_count} belum pahami")
    else:
        understood_count = understood_count + 1
        print(f"buku ke {understood_count} sudah di baca dan dipahami")

if understood_count == book_count:
    print('Bu, Semua buku sudah dibaca dan di pahami')
else:
    print(f'tidak semua buku sudah di pahami.'
          f' anak hanya bisa memahami {understood_count}')
# print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_dibaca_dan_dipahami}')
