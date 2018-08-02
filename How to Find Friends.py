def check_connection(network, friend1, friend2):
    connection = set([friend1])
    
    for _,_ in enumerate(network):
        for pair in network:
            first, second = pair.split('-')
            union = {first}|{second}
    
            if len(connection.intersection(union)):
                connection.update(union)
                
    return (friend2 in connection)