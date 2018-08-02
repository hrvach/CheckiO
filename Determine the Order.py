from itertools import product

def checkio(blocks):
    word = list(set(''.join(blocks)))    
    q = [(i,j) for b in blocks for (i,j) in product(b, b) if b.index(i)