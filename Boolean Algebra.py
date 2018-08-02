# migrated from python 2.7
def boolean(x, y, operation):
    ops = {"conjunction": '0001', "disjunction": '0111', "implication": '1011', "exclusive": '0110', "equivalence": '1001'}
    return int(ops[operation][y*2+x])
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"