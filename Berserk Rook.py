# migrated from python 2.7
from itertools import *

def nothing_inbetween(targets, x, y):    
    return not len([a_b_c for a_b_c in map(sorted, (combinations(targets | {x}, 3))) if x==a_b_c[0] and y==a_b_c[2] and (a_b_c[0][0]==a_b_c[1][0]==a_b_c[2][0] \
                    or a_b_c[0][1]==a_b_c[1][1]==a_b_c[2][1])])

def berserk_rook(berserker, enemies, level=0, path=[]):    
    row,column = list(berserker)
    targets = {enemy for enemy in enemies if row in enemy or column in enemy}    
    visible_targets = {t for t in targets if nothing_inbetween(targets, berserker, t)}
    
    if not visible_targets: return level

    return max([0]+[berserk_rook(target, enemies-{target}, level+1, path+[target]) \
                    for target in visible_targets])