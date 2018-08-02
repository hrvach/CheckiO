def factorize(n, t=[]):
    for i in range(9,1,-1):
        if n % i == 0:
            n, t = n/i, t+[str(i)]
            return factorize(n, t)
    return (n, t)
            

def checkio(number):
    residue, factors = factorize(number, [])
    return int(''.join(sorted(factors))) if residue==1 else 0