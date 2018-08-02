def recall_password(grille, password):
    password, s = map(''.join, [password, grille])

    outtext = ''
    for i in range(4):
        print (grille)
        g = [n for n,i in enumerate(''.join(grille)) if i=='X']
        outtext += ''.join(tuple(map(password.__getitem__, g)))
        grille = tuple(map(''.join, list(zip(*grille[::-1]))))       

    return outtext