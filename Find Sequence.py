# migrated from python 2.7
import re

def checkio(matrix):
    b = [[0]*i for i,_ in enumerate(matrix)]
    q = [sum(i,[]) for i in list(zip(b,matrix,b[::-1]))+list(zip(b[::-1],matrix,b))]
    return any([bool(re.search(r'([1-9])\1{3,}', ''.join(map(str, i)))) for i in matrix+list(zip(*matrix))+q+list(zip(*q))])