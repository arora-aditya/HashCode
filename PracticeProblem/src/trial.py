import numpy as np

def read_input_pizza(filename):
    """Reads the input of a Pizza problem.

    returns:

    R: number of Rows of pizza grid
    C: number of Cols of pizza grid
    L: Lowest number of each ingredients per slice
    H: Highest number of cells per slice
    pizza: the pizza grid (1 == tomato, 0 == mushroom)
    """
    lines = open(filename).readlines()
    R, C, L, H = [int(val) for val in lines[0].split()]
    pizza = np.array([list(map(lambda item: 1 if item == 'T' else 0, row.strip())) for row in lines[1:]])
    return R, C, L, H, pizza

R, C, L, H, pizza = read_input_pizza('files/a_example.in')

from pizza import Pizza
# piz = Pizza(R, C, L, H, pizza)
# piz.generate_slices()
# print(piz.convert_to_output())
# print(piz)
# # piz.insert_slice(s1)

R, C, L, H, pizza = read_input_pizza('files/b_small.in')
piz = Pizza(R, C, L, H, pizza)
piz.generate_slices()
print(piz.convert_to_output())
print(piz)
