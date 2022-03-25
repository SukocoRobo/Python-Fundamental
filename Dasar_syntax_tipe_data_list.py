"""
This is python code for syntax data list
"""
book_list = ['Seven Habits','How to influence person','First thing first','4D-X']
print('Show book list')
print(book_list)

print('\nShow book list with "for in"')
for book in book_list:
    print(book)

print('\nShow book list on index count')
print(book_list[0])
print(book_list[2])

print('\nShow book list with "For in range"')
for i in range(0, len(book_list)):
    print(book_list[i])

book_list = [1,'Dragon', -313, 3.14]
print('\nShow book list with Different variable')
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nBring back book list to first time')
book_list = ['Seven Habits','How to influence person','First thing first','4D-X']
print('\nAdd 1 new book on the list')
book_list.append('Dunia Binatang')
# print('\nShow book list with Different variable')
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nClear List')
book_list.clear()
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nGanti Element pertama pada list')
book_list = ['Seven Habits','How to influence person','First thing first','4D-X']
book_list[0] = 'Seven summits'
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nAmbil Element Ke-2 pada list')
book = book_list.pop(1)
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nBuku yang di ambil dari list')
print(book)

print('\nAmbil Element dengan pop tanpa variable')
book = book_list.pop()
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nBuku yang di ambil dari list')
print(book)