# migrated from python 2.7
from operator import sub

def hex_spiral(first, second, spiral=[[0,0,0]]*2):
    transforms = ((1,0,-1),(1,-1,0), (0,-1,1), (-1,0,1),(-1,1,0),(0,1,-1),)
    
    for i in range(max(first, second)):
        for n,t in enumerate(transforms):            
            for k in range(i-(n==1)*1):
                spiral.append(list(map(sum, list(zip(spiral[-1], t)))))

    return max(list(map(abs, list(map(sub, *[spiral[second], spiral[first]])))))