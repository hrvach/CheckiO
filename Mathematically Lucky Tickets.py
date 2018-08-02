from operator import add, mul, truediv, sub

def checkio(input):
    def f(x):
        yield int(x)    
        for i in range(1,len(x)):
            for a in f(x[:i]):
                for b in f(x[i:]):
                    for op in [add,mul,sub,truediv][:3+(int(b)!=0)]:
                        yield op(a,b)

    return all(round(i,2)!=100 for i in f(input))