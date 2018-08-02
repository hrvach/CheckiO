# migrated from python 2.7
def weak_point(m):
    x,y = list(map(sum, m)), list(map(sum, list(zip(*m))))
    return (x.index(min(x)), y.index(min(y)))