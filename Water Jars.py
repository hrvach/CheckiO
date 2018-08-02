def checkio(first, second, goal):
    (a,b), (c,d) = (0, 0), (0, 0)
    path1, path2 = [], []

    over = lambda: any((goal in (a,b), goal in (c,d)))
    
    while not over() :
        delta1, delta2 = min(a, second-b), min(first-c, d)
        (a,b), (c,d) = (a-delta1, b+delta1), (c+delta2, d-delta2)

        if over(): break
        
        if a==0:
            path1.append('01')
            a=first
        if b>=second:
            path1.append('20')
            b=0

        if c>=first:
            path2.append('10')
            c=0
        if d==0:
            path2.append('02')
            d=second

        if over(): break
        
        path2.append('21')
        path1.append('12')
        
    return path1 if goal in (a,b) else path2