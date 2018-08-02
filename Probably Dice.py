def probability(n, r, t):        
        res = a = [0]+r*[1]
        for _ in range(n-1):
                b = res
                res = [0]*(len(a)+len(b)-1)
                for i,_ in enumerate(a):
                        for j,_ in enumerate(b):
                                res[i+j] += a[i]*b[j]
        try: return res[t]*1.0/r**n
        except IndexError: return 0