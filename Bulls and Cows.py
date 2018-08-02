# migrated from python 2.7
import string
from functools import reduce

response = ((3,1), (2,2), (3,0), (2,0), (1,0), (0,0), (2,1), (1,1))

def checkio(a):
  if not len(a)>2: return ['1357', '2491', '6890'][len(a)]
  
  def count(goal, res):
    bulls = cows = 0
    for u, g in zip(res, goal):
        if u == g:
            bulls += 1
        elif u in goal:
            cows += 1
    return bulls, cows

  candidates = {str(i).zfill(4) for i in range(9999)} 
  results = dict(list(map(string.split, a)))

  bulls = {i[:4]: (int(i[5]), int(i[7])) for i in a}  

  
  conditions = [set([x for x in candidates if count(x, key)==val]) \
          for key,val in bulls.items()]
 
  conditions = reduce(set.intersection, conditions)

  bla = dict()  
  for c in conditions:            
      bla[c]=sum([len([x for x in conditions if count(x, key)==val]) for val in response])
  
  return min(bla, key=bla.get)