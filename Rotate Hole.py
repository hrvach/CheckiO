def rot(a,b):
    for n,i in enumerate(a):
        if all(a[j] for j in b): yield n
        a=[a[-1]] + a[:-1]

rotate = lambda a,b: list(rot(a,b,))