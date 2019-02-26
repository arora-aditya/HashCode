from slice import Slice
from typing import List

class DoubleSliceAtSameLocation(Exception):
    pass

class Pizza:
    def __init__(self, R:int, C:int, L:int, H:int, pizza: List[List[int]]):
        self.R, self.C = R, C
        self.L, self.H = L, H
        self.pizza: List[List[int]] = pizza
        self.is_slice: List[List[bool]] = [[False for c in r] for r in pizza]
        self.slices: List[Slice] = []

    @property
    def num_slices(self):
        return len(self.slices)

    def generate_slices(self):
        s1 = Slice(self.pizza)
        s1.expand_to_valid(self.L, self.H)
        s1.expand_more(self.H)
        # s1.shrink(self.H)
        self.insert_slice(s1)
        print(s1)
        s2 = Slice(self.pizza, sr=0, sc=s1.ec + 1)
        s2.expand_to_valid(self.L, self.H)
        s2.expand_more(self.H)
        # s2.shrink(self.H)
        self.insert_slice(s2)
        s3 = Slice(self.pizza, sr=0, sc=s2.ec + 1)
        s3.expand_to_valid(self.L, self.H)
        s3.expand_more(self.H)
        # s3.shrink(self.H)
        self.insert_slice(s3)
        s4 = Slice(self.pizza, sr=0, sc=s3.ec + 1)
        s4.expand_to_valid(self.L, self.H)
        s4.expand_more(self.H)
        # s4.shrink(self.H)
        self.insert_slice(s4)
        s5 = Slice(self.pizza, sr=0, sc=s4.ec + 1)
        s5.expand_to_valid(self.L, self.H)
        s5.expand_more(self.H)
        # s5.shrink(self.H)
        self.insert_slice(s5)
        s6 = Slice(self.pizza, sr=0, sc=s5.ec + 1)
        s6.expand_to_valid(self.L, self.H)
        s6.expand_more(self.H)
        # s6.shrink(self.H)
        self.insert_slice(s6)

    def insert_slice(self, slice: Slice):
        self.slices.append(slice)
        for i in range(slice.sr, slice.er+1):
            for j in range(slice.sc, slice.ec+1):
                if self.is_slice[i][j] == True:
                    raise DoubleSliceAtSameLocation
                self.is_slice[i][j] = True

    def __str__(self):
        st = 'pizza\n'
        for i in self.pizza:
            for j in i:
                st += str(j) + ' '
            st += '\n'
        st += 'sliced\n'
        for i in self.is_slice:
            for j in i:
                if j == False:
                    st += 'F '
                else:
                    st += 'T '
            st += '\n'
        for slice in self.slices:
            st += slice.__str__()
            st += '\n'
        return st

    def convert_to_output(self) -> str:
        st = f'{self.num_slices}\n'
        for slice in self.slices:
            st += slice.convert_to_output()
        return st




