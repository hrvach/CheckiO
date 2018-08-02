# migrated from python 2.7
font=[list(map(int, list(bin(x)[2:].zfill(15)))) for x in [31279,9184,20157,18107,28831,30386,15031,20120,32447,14014]]

def checkio(a):
    sliding_window = [sum(x,()) for x in zip(zip(*a)[1:],zip(*a)[2:],zip(*a)[3:])[::4]]
    correlation_index = [[sum([i[0]==i[1] for i in zip(a[0],a[1])]) for a in zip([row]*10,font)] for row in sliding_window]
    return int(''.join([str(i.index(max(i))) for n,i in enumerate(correlation_index) if max(i)>13]))