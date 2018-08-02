def rotate(state, wheel):
    x, a = [0, 0, 1, 5, 6][int(wheel)], list(state)
    a[x],a[2+x],a[3+x],a[5+x]=a[2+x],a[5+x],a[x],a[3+x]
    return tuple(a)

def puzzle88(state):    
    queue, history = [('', state)], set()
    while len(queue):        
        rotations, wheel_state = queue.pop(0)
        
        if wheel_state not in history:            
            queue+=[(rotations + wheel, rotate(wheel_state, wheel)) for wheel in '4231']
            history.add(wheel_state)
            if wheel_state == (1,2,1,0,2,0,0,3,0,4,3,4): return rotations