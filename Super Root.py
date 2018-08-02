from math import exp as e,log as l
def super_root(n):
    f=lambda w,x: w if (e(w)*w-x)/(w*e(w)+e(w))<=10e-15 else f(w-(e(w)*w-x)/(w*e(w)+e(w)),x)
    return e(f(*[l(n)]*2))