from numpy import reshape
from typing import List, Optional

class Slice:
    def __init__(self,
                 pizza: List[List[int]],
                 sr: Optional[int] = 0,
                 sc: Optional[int] = 0,
                 er: Optional[int] = 0,
                 ec: Optional[int] = 0):
        self.pizza = pizza
        self.dims = (len(pizza), len(pizza[0]))
        self.sr = sr
        self.sc = sc
        self.er = er
        self.ec = ec

    @property
    def l(self):
        return self.ec - self.sc

    @property
    def w(self):
        return self.er - self.sr

    @property
    def slice(self):
        slice = []
        for i in range(self.sr, self.er):
            for j in range(self.sc, self.ec):
                slice.append(self.pizza[i][j])
        return slice

    @property
    def can_expand_r(self):
        return self.er < self.dims[0] - 1

    @property
    def can_expand_c(self):
        return self.ec < self.dims[1] - 1

    def expand_to_valid(self, minI: int, maxS: int):
        while self.can_expand_r and self.can_expand_c and len(self.slice) - 1 < maxS and not self.is_valid(minI, maxS):
            if self.can_expand_r:
                self.er += 1
            if self.can_expand_c:
                self.ec += 1

    def expand_more(self, maxS: int):
        if self.w != 0:
            tops = (maxS - len(self.slice))/self.w
        else:
            tops = pow(maxS, 0.5)
        while tops > 0 and self.l + len(self.slice) < maxS and self.can_expand_r and self.is_valid(-1, maxS):
            self.er += 1
            tops -= 1
        if self.l != 0:
            tops = (maxS - len(self.slice)) / self.l
        else:
            tops = pow(maxS, 0.5)
        while tops > 0 and self.w + len(self.slice) < maxS and self.can_expand_c and self.is_valid(-1, maxS):
            self.ec += 1
            tops -= 1
        print(self)

    def shrink(self, maxS: int):
        while len(self.slice) > maxS:
            if self.w > self.l:
                self.er -= 1
            else:
                self.ec -= 1

    def is_valid(self, minI: int, maxS: int):
        return (self.slice.count(1) >= minI and
                self.slice.count(0) >= minI)

    def convert_to_output(self):
        return f'{self.sr} {self.sc} {self.er} {self.ec}\n'

    def __str__(self):
        if self.l != 0 and self.w != 0:
            slice_st = reshape(self.slice, (self.w, self.l))
        else:
            slice_st = '[]'
        st = f'length:{self.l}\n' + f'width:{self.w}\n' + f'coordinates:{(self.sr, self.sc)}, {(self.er, self.ec)})\n' + f'slice:\n{slice_st}'
        return st
