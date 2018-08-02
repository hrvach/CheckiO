from itertools import *

def life_counter(state, tick_n):    
    cells = {divmod(n, len(state[0])) for n,i in enumerate(sum(state,())) if i}
    adjacent = set(product(*[(0,-1,1)]*2))-{(0,0)}
        
    for tick in range(tick_n):
        near = lambda x,y: sum([1 if abs(y-c[1])<=1 and abs(x-c[0])<=1
                                else 0 for c in cells-{(x,y)}])

        empty = {(i+x,j+y) for (i,j) in cells for (x,y) in adjacent} - cells
        
        born = {cell for cell in empty if near(*cell)==3}
        live = {cell for cell in cells if 1<4}

        cells = (born | live)        

    return len(cells)