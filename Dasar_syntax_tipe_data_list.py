"""
This is python code for syntax data list
"""
book_list = ['Seven Habits','How to influence person','First thing first']
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
