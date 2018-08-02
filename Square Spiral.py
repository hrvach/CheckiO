def find_distance(first, second):
    loc = [0, 0]
    
    for i in range(first+second):
        for j in (i//2)*[(-1j)**(i+1)]:            
            loc.append(loc[-1]+j)
    
    d = loc[first]-loc[second]
    return (abs(d.real)+abs(d.imag))