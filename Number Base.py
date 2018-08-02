# migrated from python 2.7
def checkio(str_number, radix):
    try: return sum([i*radix**n for n,i in enumerate(reversed([int(x, radix) for x in list(str_number)]))])
    except: return -1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"