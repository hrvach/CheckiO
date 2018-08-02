# migrated from python 2.7
import re
from math import radians, cos, sin, asin, sqrt

def distance(a,b):
    coords = [[int(i) if i.isdigit() else i for i in re.split('\W+', j)] for j in re.split('[,\s]+', (a+' '+b))]
    c = [radians(x[0]+x[1]/60.0+x[2]/3600.0)*[-1,1][x[3] in 'NE'] for x in coords]
    return 2*6371*asin(sqrt(sin((c[2]-c[0])/2)**2 + cos(c[0]) * cos(c[2]) * sin((c[3]-c[1])/2)**2))