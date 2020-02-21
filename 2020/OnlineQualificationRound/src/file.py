from typing import List, Dict
from book import Book
from library import Library

class File:
    def __init__(self,
                 books: Dict[int, int],
                 libraries: List,
                 days: int,):
        self.books = books
        self.libraries = libraries
        self.days = days
    
    def __str__(self):
        ret_val = f"Number of days: {self.days}\nBooks:\n"
        
        for book in self.books:
            ret_val += book.__str__() + "\n"
        ret_val += "Libraries\n"
        for library in self.libraries:
            ret_val += library.__str__() + "\n"
        return ret_val
            

def read_input_file(filename: str) -> File:
    """Reads the data of input problem

    returns:
    D: number of days,
    LIBS: list of Library objects,
    BOOKS: list of Book objects,
    """
    lines = list(map(lambda x: [int(y) for y in x.strip().split()], open(filename).readlines()))
    book_count, libs_count, days = lines[0]
    books = []
    for idx, score in enumerate(lines[1]):
        books.append(Book(idx, score))
    assert len(books) == len(lines[1])
    
    libraries = []
    for i in range(2, len(lines), 2):
        if len(lines[i]) == 0:
            continue
        num_books, signup_delay, books_per_day = lines[i]
        
        lib_books = list(map(lambda x: books[x], lines[i+1]))
        assert len(lib_books) == num_books, f"Incorrect parsing of {line[i]}"
        libraries.append(Library((i-2)//2, signup_delay, lib_books, books_per_day))
    
    return File(books, libraries, days)
    
def get_library_with_max_total_value_over_signup_time(file):
    ma = None
    for library in file.libraries:
        if ma == None:
            ma = library
        elif ma.total_value()/ma.signup_delay < library.total_value()/library.signup_delay:
            ma = library
    return ma

    
def get_library_with_min_signup_time_and_max_total_value(file):
    mi = None
    for file in file.libraries:
        if mi is None:
            mi = file
        elif (file.signup_delay, -1*file.total_value()) < (mi.signup_delay, -1*mi.total_value()):
            mi = file
    return mi

def get_library_with_max_remaining_value_over_signup_time(file, remaining_days):
    ma = None
    for file in file.libraries:
        if ma is None:
            ma = file
        elif (file.remaining_value(remaining_days - file.signup_delay)/file.signup_delay) < (ma.remaining_value(remaining_days - ma.signup_delay)/ma.signup_delay):
            ma = file
    return ma
            
            
            
        
        
    