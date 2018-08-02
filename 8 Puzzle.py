POSSIBLE = ['RD','LRD','LD','URD','LRUD','LUD','UR','LUR','UL']
M = {'D': 3, 'L': -1, 'R': 1, 'U': -3}
GOAL = [1,2,3,4,5,6,7,8,0]

from collections import deque

def checkio(state):
    q = deque()
    state = sum(state, [])
    
    q.append((state, ''))
    history=set()

    def heur(state):        
        s = state[:]
        tally=0
        for i in s:
            if i==0: continue
            (x1,y1),(x2,y2) = divmod(s.index(i),3), divmod(GOAL.index(i), 3)
            tally += abs(x2-x1)+abs(y2-y1)
        return tally
   
    while q:
        state, path = q.popleft()
        if state == GOAL:
            return path
        
        x = state.index(0)

        unsorted = []
        for key, value in zip('DLRU', (3,-1,1,-3)):
            if key in POSSIBLE[x]:
                new = state[:]
                new[x],new[x+value]=new[x+value],0                

                if str(new) not in history:
                    unsorted.append((heur(new),(new, path+key)))
                    history.add(str(new))                

        for i in sorted(unsorted):
            q.append(i[1])