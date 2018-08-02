def checkio(number):
    pigeons = [0]
    for add in range(2, 10**5):
        for n in range(len(pigeons)): 
            pigeons[n] += 1        
            number-=1
            if number < 1: return len([p for p in pigeons if p>0])

        pigeons += [0]*(add)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"