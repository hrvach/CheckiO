from math import atan2
ccw = lambda a,b,c: (b[0]-a[0])*(c[1]-a[1]) > (b[1]-a[1])*(c[0]-a[0])

def checkio(points):
    origin_point = min(points, key=lambda x: (x[1], x[0]))
    s = lambda x: (atan2(origin_point[0]-x[0], origin_point[1]-x[1]), origin_point[0]-x[0])
    
    data = sorted(points, key=s)
    shift = data.index(origin_point)
    data = data[shift:] + data[:shift]

    convex = data[:3]
    for i in data[3:]:
        while ccw(convex[-2], convex[-1], i):
            convex.pop()
        if not convex or convex[-1] != i:
            convex.append(i)
    
    offset = convex.index(min(convex))
    convex = convex[offset:] + convex[:offset]
    return [points.index(i) for i in convex]