def checkio(data):
    s = lambda b,z: '' if not z else str(s(b%z[0][0], z[1:])) + (b//z[0][0])*z[0][1]    
    return s(data, [(1000, 'M'), (900, 'MC'), (500, 'D'), (400, 'DC'), (100, 'C'), (90, 'CX'), (50, 'L'), (40, 'LX'), (10, 'X'), (9, 'XI'), (5, 'V'), (4, 'VI'), (1, 'I')])[::-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'