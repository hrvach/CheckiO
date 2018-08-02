f=lambda s:s[-1]+max(f(s[:-1]),f(s[:-2])) if s else [0,1][len(s)]
checkio=lambda a:f(a+[0])