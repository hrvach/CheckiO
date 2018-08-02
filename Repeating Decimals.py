def convert(n, d, stringify = lambda a: ''.join(list(map(str, a)))):
    whole = n//d
    n = n - whole * d
    
    history = [divmod(n, d)]
    while True: 
        c = divmod(history[-1][1]*10, d)
        history.append(c)
        if c in history[:-1]: break

    quotients, remainders = map(stringify, list(zip(*history)))
    r = quotients[1:].index(quotients[-1])+1
    res = str(whole) + '.'

    if len(history)>2:
        if history[-1]==(0,0):
            res += quotients[1:-2]
        else:
            res += '{0}({1})'.format(quotients[1:r], quotients[r:-1])                    

    return res