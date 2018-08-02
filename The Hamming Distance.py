def checkio(a, b):
    return sum((1 if x!=y else 0 for x,y in zip(format(a, '#022b')[2:], format(b, '#022b')[2:])))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"