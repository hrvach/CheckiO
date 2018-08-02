def checkio(number):
    for i in range(1,37):
        try:
            if not int(number, i) % (i-1):
                return i
        except ValueError: pass
        
    return 0