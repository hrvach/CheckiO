def move(t,n,shift=lambda c:[i for i in c if i]+[0]*c.count(0),rot=lambda t:map(list,zip(*t[::-1]))):
    diff = t = t[:]
    for i in range(n): t=rot(t) 
	for i in range(4): 
		t[i] = shift(t[i])
		for j in range(3):
			if t[i][j+1]==t[i][j]: t[i][j], t[i][j+1] = 2*t[i][j], 0
		t[i] = shift(t[i])
	for i in range(4-n): t=rot(t)   
	return (t, 1 if t != diff else 0)


def move2048(state, d):
    direction={'left': 0, 'down': 1, 'right': 2, 'up': 3}
    state, changed = move(state, direction[d])
    
    if 2048 in sum(state, []): return [list('UWIN')]*4
    
    try: 
        last_zero = 15-sum(state, [])[::-1].index(0)
        state[last_zero//4][last_zero%4] = 2
    except ValueError:
        if not changed: return [list('GAME'),list('OVER')]*2
        
    return state