# migrated from python 2.7
import copy
           
def recursive(square, digits):
    vectors = square + list(zip(*square)) + list(zip(*[(row[i],row[~i]) for i,row in enumerate(square)]))
    sums = lambda square: list(map(sum, vectors))
            
    order = len(square)
    magic = [0,0,0,15,34,65][order] # -> magic numbers for squares of order n=3,4,5
    
    for vector in zip(vectors, sums(square)):
        if not 0 in vector[0] and vector[1] != magic:
            return
    
    try:
        first_zero = sum(square, []).index(0)
    except ValueError:
        if not all([s==magic for s in sums(square)]):
            return
        else:
            return square

    new_element = dict(list(zip(('row', 'col'), divmod(first_zero, len(square)))))

    for digit in digits:                   
        square = copy.deepcopy(square)        
        square[new_element['row']][new_element['col']] = digit
        if all(i<=magic for i in sums(square)):
            r = recursive(square, digits-{digit})
            if r: return r

def checkio(matrix):
    return recursive(matrix, set(range(1,len(matrix)**2+1))-set(sum(matrix, [])))