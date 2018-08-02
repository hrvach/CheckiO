row_col_box=[set([i for i in range(81) if any([i%9==j%9, i//9==j//9, (i//27,i%9//3)==(j//27,j%9//3)])]) for j in range(81)]

def S(q):
    try: 
        n = q.index(0)
	    for x in set(range(1,10))-set([q[t] for t in row_col_box[n] if q[t]!=0]):
	    	for j in S(q[:n] + [x] + q[n+1:]): yield j
    except ValueError: yield q

def checkio(grid):
    b = list(S(sum(grid, [])))[0]
    return [b[i:i+9] for i in range(81)[::9]]