def checkio(data):
    return '{:02b} {:04b} : {:03b} {:04b} : {:03b} {:04b}'.format(*list(map(int,list("".join([i.zfill(2) for i in data.split(':')]))))).replace('0', '.').replace('1', '-')


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"