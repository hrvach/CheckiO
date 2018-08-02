# migrated from python 2.7
from itertools import combinations

def break_rings(rings):
    max_remainder = 0
    ring_elements = set.union(*rings)

    all_possible_solutions = sum([list(combinations(ring_elements, n)) \
                                  for n in range(1,len(ring_elements)+1)], [])

    for solution in all_possible_solutions:
        remaining = [i-set(solution) for i in rings]
        
        if max(list(map(len, remaining)))<2 and len(set.union(*remaining)) > max_remainder:
                max_remainder = len(set.union(*remaining))

    return len(ring_elements)-max_remainder