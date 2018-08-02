# migrated from python 2.7
from functools import reduce
def checkio(number):
    return reduce(lambda x,y: x*y, [int(i) for i in list(str(number)) if i!='0'])
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1