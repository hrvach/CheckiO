from itertools import *

def partition(n,k,l=1):
    if k<1: raise StopIteration
    if k == 1:
        if n >= l:
            yield (n,)
        raise StopIteration
    for i in range(l,n+1):
        for result in partition(n-i,k-1,i):
            yield (i,)+result

def winning_die(enemy):
    total, sides = sum(enemy), len(enemy)
    generator = partition(total, sides)

    win = dict()
    
    for player in generator:
        all_dice = list(product(enemy, player))
        score = sum([1*(x<=0: return []
    return best_option
 

if __name__ == '__main__':
    #These are only used for self-checking and not necessary for auto-testing
    def check_solution(func, enemy):
        player = func(enemy)
        total = 0
        for p in player:
            for e in enemy:
                if p > e:
                    total += 1
                elif p < e:
                    total -= 1
        return total > 0

    assert check_solution(winning_die, [3, 3, 3, 3, 6, 6]), "Threes and Sixes"
    assert check_solution(winning_die, [4, 4, 4, 4, 4, 4]), "All Fours"
    assert check_solution(winning_die, [1, 1, 1, 4]), "Unities and Four"
    assert winning_die([1, 2, 3, 4, 5, 6]) == [], "All in row -- No die"