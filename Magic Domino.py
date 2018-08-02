# migrated from python 2.7
from itertools import *
from random import shuffle

split = lambda what: [what[i:i + 2] for i in range(0, len(what), 2)]

def recursive_search(magic_square, columns_left, number, size, level=0):

    if level>size: return None
        
    diagonals = list(map(sum, list(zip(*[(row[i],row[~i]) for i,row in enumerate(magic_square)]))))
    row_sums = list(map(sum, list(zip(*magic_square))))

    if any([2*number < i for i in map(sum, [sum(i, ()) for i in split(magic_square)])]):
        return None

    if any([i>number for i in row_sums + diagonals]):
        return None

    if level == size and set(row_sums+diagonals)=={number}:
        return magic_square

    used_dominos = sum([split(col) for col in magic_square], [])
    
    for col in columns_left:
        column_permutations = iter(shuffle_column(col, size))
        for permuted in column_permutations:
            if any([i in used_dominos or i[::-1] in used_dominos for i in split(permuted)]):
                continue
            
            r = recursive_search(magic_square+[permuted], columns_left-{col}, number, size, level+1)
            if r: return r
    
def shuffle_column(col, size):
    perms_list=list(permutations([list(permutations(i)) for i in split(col)]))
    shuffle(perms_list)
    for p in perms_list:
        for r in tuple(product(*p)):
            yield sum(r, ())
    

def magic_domino(size, number):
    dominoes = [(i,j) for i in range(7) for j in range(7) if i<=j]
    possible_columns = {col for col in combinations(dominoes, size//2) if sum(map(sum, col))==number}
  
    cols = {sum(i, ()) for i in possible_columns}

    return tuple(zip(*recursive_search([], cols, number, size, 0)))