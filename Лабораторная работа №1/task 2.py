# TODO Найдите количество книг, которое можно разместить на дискете
code_in_byte = 4
line = 25
page = 50
book = 100
disk = 1.44

book_size = book * page * line * code_in_byte
books_in_disk = (disk * 1024 * 1024) // book_size
print(f"Количество книг, помещающихся на дискету: {books_in_disk:.0f}")
