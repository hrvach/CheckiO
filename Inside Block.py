m = lambda (a,b),(x,y),(c,d): cmp((y-b)*(c-x),(d-y)*(x-a))
def is_inside(q, p, c=cmp):
    t=0
    for i,j,k in zip(q[-1:]+q[1:], q, q[1:]+q[:1]):
        t += [(c(p,i)==c(p,k))*m(i,k,j),0,m(j,p,k)][c(j,p)*c(k,p)]
    return t!=0