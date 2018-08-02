def count_gold(p):
    return reduce(lambda x,y: tuple(i+max(x[n], x[n+1]) for n,i in enumerate(y)), p[::-1])[0]