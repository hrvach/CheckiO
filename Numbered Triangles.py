from itertools import *

tree = lambda t,p,s,n=0,v=0: len(t) and max([0]+[tree(t[:z]+t[z+1:], r, 
        s+m, n+1, v) for z,k in enumerate(t) for l,m,r in set(permutations(k)) \
        if p==l and (len(t)>1 or r==v)]) or (0 if n<6 else s)

def checkio(triangles):
    return max(tree(triangles, a, 0, 0, a) for a,b,c in permutations(triangles[0]))