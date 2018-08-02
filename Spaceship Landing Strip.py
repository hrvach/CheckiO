# migrated from python 2.7
def psum(matrica):
    s = matrica[0]
    yield s
    for i in matrica[1:]:
        s = [0 if not x_y[1] else x_y[0]+x_y[1] for x_y in zip(s,i)]
        yield s

def lra(his):
    area=0
    for i,m in enumerate(his):
        for j,v in enumerate(his[i:]):
            m = min(v, m)
            area = max(m*j+m, area)
    return area
    
def checkio(a):
    mapa = list([[1 if i in 'GS' else 0 for i in l] for l in a])
    return max(list(map(lra, psum(mapa))))