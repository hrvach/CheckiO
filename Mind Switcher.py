from functools import reduce

def mind_switcher(journal):
    robots = {i:i for i in reduce(set.union, journal)}    
    
    for x,y in journal:
        robots[x], robots[y] = robots[y], robots[x]

    cycles = []    
    while robots:            
        body, mind = robots.popitem()
        cycles.append([(body, mind)])
        
        while robots.get(mind) != None:
            body, mind = mind, robots.get(mind)        
            cycles[-1].append((body, mind))
            robots.pop(body)

    cycles = [reduce(lambda x,y: x+y[1:], i[:-1]) for i in cycles if i[:-1]]    
    
    output = []
    for i in cycles:
        output += [{'nikola', i[-1]}] + [{'sophia', k} for k in i] + [{'nikola', i[0]}]

    if len(cycles) % 2: output.append({'nikola', 'sophia'})
    
    return output