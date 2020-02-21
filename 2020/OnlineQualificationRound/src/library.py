from math import ceil
from collections import defaultdict, Counter
from typing import List, Dict


class Library:
    def __init__(self, idx: int, signup_delay: int, books: List, books_per_day: int):
        self.idx = idx
        self.signup_delay = signup_delay
        self.books = books
        self.book_per_day = books_per_day
    
    def __str__(self):
        return f"L IDX:{self.idx} Bs:{[book.idx for book in self.books]} BPD:{self.book_per_day}"

    # total value of all books in library
    def total_value(self):
        return sum(map(lambda x: x.score, filter(lambda x: x.seen == False, self.books)))
    
    # total value of all books in library
    def remaining_value(self, remaining_days):
        counter = 0
        su = 0
        for book in self.books:
            if remaining_days <= 0:
                break
            if book.seen == False:
                su += book.score
                if counter == self.book_per_day:
                    counter = 0
                    remaining_days -= 1
            
        return su

    # all books in library
    def total_books(self):
        return len(self.books) 

    # how much time to completely scan every book in library
    def completion_time(self):
        return self.signup_delay + ceil(len(self.books)/self.book_per_day)

    # how much we get out of it 
    def value_per_signup(self):
        return self.total_value()/self.signup_delay

    def to_file(self):
        if len(self.books) > 0:
            assert len(f"{self.idx} {len(self.books)}") > 0
            return f"{self.idx} {len(self.books)}\n{' '.join([str(x.idx) for x in self.books])}\n"
        return ""