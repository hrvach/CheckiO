# migrated from python 2.7
from itertools import permutations, starmap

neighbors = lambda a,b: len([x_y for x_y in zip(*list(map(str, [a,b]))) if x_y[0]!=x_y[1]]) == 1
def checkio(numbers):
    l = 1
    while l