import re
from random import choice, random, shuffle
from time import time

from itertools import *
from functools import reduce

DIRS = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

def supply_routes(chart):
    board = {(i, j) for j in range(len(chart[0])) for i in range(len(chart))}

    finder = lambda x: {(i, j) for i,j in board if chart[i][j]==x}
    obstacles, *stations, factory, clear = map(finder, 'X1234F.')

    stations = [i.pop() for i in stations]

    adjacent = {(0,1), (1,0), (0,-1), (-1,0)}
    direction = {(0,1): 'E', (1,0): 'S', (0,-1): 'W', (-1,0): 'N'}
    nearby = lambda x,y: {(x+a, y+b) for a,b in adjacent}
    grow=lambda s: reduce(set.union, list(starmap(nearby, s))) if s else set()

    factory_terminals = grow(factory)
    #clear = clear - factory_terminals
    factory = factory.pop()
      
    
    def does_path_exist(cell, clear, target):
        area = [set(), set(), {cell}]    
        while area[-1]-area[-2] and not area[0].intersection(target):
            increase = (grow(area[-1]) - area[-2]) & (clear|{factory})
            area.append(increase-area[0])
            area[0] |= increase
      
        return factory in area[0]

    manhattan_distance = lambda cell: abs(factory[0] - cell[0]) + abs(factory[1] - cell[1])
    heur = lambda cells: sorted(cells, key=manhattan_distance, reverse=False)

    timer = time()

    def dfs(current_cell, target, clear, stations, path='', level=0):        
        if time()-timer > 1:
            return False
        if level > 40: return False
        if len(re.sub(r'(\w)\1+', r'\1', 'path'))>9: return False # No more than 8 turns        
        if not all(does_path_exist(i, clear, {factory}) for i in stations): # if others can't finish, drop it
            return False
        if not all(does_path_exist(i, clear, stations) for i in factory_terminals): # if others can't finish, drop it
            return False

        if current_cell == factory:
            yield (clear, path)
            return 
        
        candidates = nearby(*current_cell).intersection(clear|{factory})
        ordering = heur(candidates)
        try:            
            next_straight_cell = ({tuple(map(sum, zip(DIRS[path[-1]], current_cell)))} & candidates).pop()
            ordering.remove(next_straight_cell)
            ordering = [next_straight_cell] + ordering

            for o in ordering:
                if manhattan_distance(o)<2:
                    ordering.remove(o)
                    ordering = [o] + ordering
                    shuffle(ordering)
                             
        except:
            ordering = heur(candidates)
            shuffle(ordering)
           
        
        for candidate in ordering:
            letter = direction[(candidate[0]-current_cell[0], candidate[1]-current_cell[1])]

            for c in dfs(candidate, target, clear-{candidate}, stations, path+letter, level+1):
                if c: yield c

    stations_list = list(permutations(stations))
    shuffle(stations_list)

    for station in stations_list:        
        for target in factory_terminals:
            timer = time()
            for c0,r0 in dfs(station[0], target, clear, set(station[1:])):
                for c1,r1 in dfs(station[1], target, c0, set(station[2:])):
                    for c2,r2 in dfs(station[2], target, c1, set(station[3:])):
                        for c3,r3 in dfs(station[3], target, c2, set()):
                            res = [r0, r1, r2, r3]
                            res = sorted(list(zip(res, station)), key=lambda x: stations.index(x[1]))
                            return [i[0] for i in res]