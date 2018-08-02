# migrated from python 2.7
from itertools import *
from functools import reduce

def healthy(grid):    
    all_cells = {(row,col) for col in range(len(grid[0])) for row in range(len(grid))}
    germs = {(i,j) for (i,j) in all_cells if grid[i][j]==1}
    nearby = lambda x, y: {(x-1, y), (x+1, y), (x, y-1), (x, y+1)}
        
    def find_max(grid, grow=lambda s: reduce(set.union, list(starmap(nearby, s)))):
        for cell in germs:
            area = [set(), {cell}]
            for size in takewhile(lambda size: area[-1].issubset(germs), count()):
                area.append(grow(area[-1]) - area[-2])
            if area[-1].intersection(germs):
                size, cell = 0, (0,0)                
            yield (size, cell)            
          
    return max(list(find_max(grid))+[(0, (0,0))], key=lambda x: x[0])[1]