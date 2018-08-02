from itertools import *
from functools import reduce
from copy import deepcopy

def lanterns_flow(river_map, minutes):
    board = {(i, j) for j in range(len(river_map[0])) for i in range(len(river_map))}
    obstacles, clear = map(lambda x: {(i,j) for i,j in board if river_map[i][j]==x}, 'X.')
    river = deepcopy(clear)
    
    nearby = lambda x,y: {(x+a, y+b) for a,b in set(product(*[(0,-1,1)]*2))}
    grow=lambda s: reduce(set.union, list(starmap(nearby, s)))

    # Find left wall
    area = [set(), {(0,0)}]
    while area[-1]-area[-2]:
        increase = (grow(area[-1]) - area[-2]) & obstacles
        area.append(increase)
    left_wall = reduce(set.union, area)
    
    # Grow race tracks
    race_tracks = [set(), left_wall]
    while race_tracks[-1]-race_tracks[-2]:
        race_tracks.append(grow(race_tracks[-1]) & clear)
        clear = clear - race_tracks[-1]

    def sortpath(path):
        outpath = [min(path)]
        path.remove(outpath[-1])
        while path:
            nearby = lambda x,y: {(x+a, y+b) for a,b in [(-1,0), (1,0), (0,1), (0,-1)]}
            outpath.append((nearby(*outpath[-1]) & path).pop())
            path.remove(outpath[-1])
            
        return outpath

    lanterns = {(sortpath(t)[minutes]) for t in race_tracks[2:-1]}
    return len(grow(lanterns) & river)