# migrated from python 2.7
def checkio(a):
    return abs(sum([x[0][0]*x[1][1]-x[1][0]*x[0][1] for x in zip(a, a[1:]+a[:1])])/2.0)