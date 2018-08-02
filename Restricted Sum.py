def checkio(data):
    if not len(data): return 0
    return data[0] + checkio(data[1:])