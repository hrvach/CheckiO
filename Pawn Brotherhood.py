def get_attackers(p):
    a,b = map(ord, p)
    return {chr(a-1)+chr(b-1),chr(a+1)+chr(b-1)}    
    
def safe_pawns(pawns):
    return len(pawns)-sum([0 if pawns&(get_attackers(p)) else 1 for p in pawns])