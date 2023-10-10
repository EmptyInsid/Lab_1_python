#задание 2: Расчет количества книг на дискете

DIFF_SIZE = 2**10
BYTE_CHAR = 4

mb_info_in_disk = 1.44
bytes_in_disk = mb_info_in_disk * DIFF_SIZE * DIFF_SIZE

count_of_pages = 100
count_of_str_in_page = 50
count_of_char_in_str = 25

bytes_for_str = BYTE_CHAR * count_of_char_in_str
bytes_for_page = bytes_for_str * count_of_str_in_page
bytes_for_book = bytes_for_page * count_of_pages

count_of_books_in_disk = int(bytes_in_disk // bytes_for_book)

print("Количество книг, помещающихся на дискету:", count_of_books_in_disk)
