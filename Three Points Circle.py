def checkio(data):
    a,b,c = eval(data)
    perms = [(a,b,c), (a,c,b), (b,a,c), (b,c,a), (c,a,b), (c,b,a)]
    
    for i in range(6):
        try:
            s_ab, s_bc = (b[1]-a[1])/(b[0]-a[0]), (c[1]-b[1])/(c[0]-b[0])
    
            x = (s_ab*s_bc*(a[1]-c[1])+s_bc*(a[0]+b[0])-s_ab*(b[0]+c[0]))/(2*(s_bc-s_ab))
            y = -1*(x-(a[0]+b[0])/2)/s_ab + (a[1]+b[1])/2
        
            r = ((b[0]-x)**2+(b[1]-y)**2)**0.5
            break
        except ZeroDivisionError:
            a,b,c=perms.pop()
    
    x,y,r = map(lambda x: '{0:g}'.format(float('{0:.2f}'.format(x))), (x,y,r))
    return "(x-{0})^2+(y-{1})^2={2}^2".format(x,y,r)