class Friends:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        return set.union(*self.connections)

    def connected(self, name):
        return set.union(*[i.difference({name}) for i in self.connections if name in i]+[set()])