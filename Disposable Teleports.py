def checkio(teleports_string):
    teleports, paths = {frozenset(i) for i in teleports_string.split(',')}, []

    def walk(station, links, path):
        if len(set(path)) == 8 and station == '1':
            paths.append(path+station)
        for link in filter(lambda x: station in x, links):
            walk(next(iter(link-{station})), links-{link}, path+station)

    walk('1', teleports, '')
    return min(paths, key=len)