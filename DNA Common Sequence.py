cache = dict()

longest = lambda m: 0 if not m else len(max(m, key=len))
  
def subseqs(a, b):
    if not a or not b:
        return {''}

    key = cache.get((a, b))

    if key is not None:
        return key

    cache[(a,b)] = ({a[0] + i for i in subseqs(a[1:], b[1:])} if a[0]==b[0] \
        else subseqs(a, b[1:]) | subseqs(a[1:], b))

    return {i for i in cache[(a,b)] if len(i) == longest(cache[(a,b)])}

def common(first, second):
    cache.clear()
    s = subseqs(first, second)        
    return  ','.join(i for i in sorted(list(s)) if len(i) == longest(s))