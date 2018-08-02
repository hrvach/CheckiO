def det(m):
    if len(m) < 2: return m[0][0]
    if len(m) == 2: return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    
    b = [i[1:] for i in m]
    minors = [b[0:n]+b[n+1:] for n,_ in enumerate(b)]    
    coefficients = [i[0]*(-1)**n for n,i in enumerate(m)]
    
    return sum([coefficients[i]*det(minors[i]) for i,_ in enumerate(m)])
    
def checkio(m):
    return det(m)