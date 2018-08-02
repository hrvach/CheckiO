from collections import Counter

def find_cycle(connections):
    nodes = set(sum(connections, ()))
    links, paths = {frozenset(i) for i in connections}, [[]]
    
    freq = 1
    while freq == 1:
        try:
            node, freq = Counter(sum(connections, ())).most_common()[-1]
        except IndexError:
            return []
        if freq == 1:
            nodes = nodes - {node}
            connections = [i for i in connections if node not in i]

    
    def walk(node, links, path):
        if len(set(path)) < len(path): return
        if path and node == path[0] and len(path) >= len(max(paths,key=len)):
            paths.append(path+[node])

        for link in filter(lambda x: node in x, links):
            walk(next(iter(link-{node})), links-{link}, path+[node])

    for node in nodes:
        if node not in sum(paths, []):
            walk(node, links, [])

    return max(paths, key=len)