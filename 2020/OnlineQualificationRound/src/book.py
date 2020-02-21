from collections import namedtuple

class Book:
    def __init__(self, idx: int, score: int):
        self.idx = idx
        self.score = score
        self.seen = False
    
    def __str__(self):
        return f"B I:{self.idx} S:{self.score}"
        