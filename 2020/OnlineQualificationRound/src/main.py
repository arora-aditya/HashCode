import os
from file import (
    File, 
    read_input_file, 
    get_library_with_max_total_value_over_signup_time,
    get_library_with_min_signup_time_and_max_total_value,
    get_library_with_max_remaining_value_over_signup_time,
    )
from solution import Solution
from datetime import datetime

import pickle

filenames = [
    # 'a_example',
    # 'b_read_on',
    # 'c_incunabula',
    # 'd_tough_choices',
    'e_so_many_books',
    # 'f_libraries_of_the_world'
]
output_directory = f"../output/output_{str(datetime.now()).replace(' ', '_')[:-7]}"

for filename in filenames:
    print(filename)
    file_object = read_input_file(f'../files/{filename}.txt')

    # maximum score per time, maximum time
    library = get_library_with_min_signup_time_and_max_total_value(file_object)
    remaining_days = file_object.days - library.signup_delay
    number_of_days_passed_for_lib = library.signup_delay
    seen_books = set()
    unseen_books = set()
    counter = 0
    
    for book in sorted(library.books, key=lambda x: x.score, reverse=True):
        if number_of_days_passed_for_lib >= remaining_days:
            break
        if book not in seen_books:
            seen_books.add(book)
            book.seen = True
            unseen_books.add(book)
            counter += 1
            if counter % library.book_per_day == 0:
                number_of_days_passed_for_lib += 1
                counter = 0
                
    for i in range(1, len(file_object.libraries)):
        unseen_books = set()
        print(i/len(file_object.libraries), end=' '*10+'\r')
        library = get_library_with_max_remaining_value_over_signup_time(file_object, remaining_days)
        number_of_days_passed_for_lib = library.signup_delay
        for book in sorted(library.books, key=lambda x: x.score, reverse=True):
            if number_of_days_passed_for_lib >= remaining_days:
                break
            if book not in seen_books:
                seen_books.add(book)
                book.seen = True
                book.score = 0
                unseen_books.add(book)
                counter += 1
                if counter % library.book_per_day == 0:
                    number_of_days_passed_for_lib += 1
                    counter = 0
                    
        library.books = list(sorted(unseen_books, key=lambda x: x.score, reverse=True))
        # libraries.append(library)
        # print([b.score for b in library.books])
            
    
    s = Solution(output_directory, filename, file_object.libraries)
    s.to_file()
    print(filename, 'done')

os.system(f'zip -r {output_directory}/archive.zip main.py solution.py library.py file.py book.py')
print(f'{output_directory}/')





