from itertools import zip_longest

class Poly(object):     
    def __init__(self, coeffs=[0,1]): self.deg, self.c = len(coeffs)-1, coeffs
    def __repr__(self):
        res = ''.join([['+','-'][bool(i<0)]+
        [str(abs(i))+'*x', 'x'][bool(i in [1,-1])]*bool(n>0) +
        '**%s'%n*bool(n>1) + bool(n==0)*str(abs(i)) 
        for n,i in enumerate(self.c) if i][::-1]).strip('+').replace('+-','-')
        
        if not res: return '0'
        return res.strip('+')
    def __add__(self, other):
        if type(other)==int: other=Poly([other])
        return Poly(list(map(sum, zip_longest(self.c,other.c,fillvalue=0))))
         
    def __mul__(self, other):
        if type(other)==int: other=Poly([other])
        coeffs = [0]*(self.deg + other.deg + 1)
        for i,s1 in enumerate(self.c):
            for j,c1 in enumerate(other.c):
                coeffs[i+j] += s1*c1        

        return Poly(coeffs)

    def __sub__(self, other):
        if type(other)==int: other=Poly([other])        
        return self.__add__(other.__neg__())

    def __neg__(self): return Poly([-i for i in self.c])
    def __rsub__(self, other): return -self.__add__(-other)

    __rmul__, __radd__= __mul__, __add__
        
def simplify(text):
    return str(eval(text.replace('x', 'Poly()')))