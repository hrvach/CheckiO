def checkio(lines_list):
    lines_list = [sorted(i) for i in lines_list]
    return sum([all(i in lines_list for i in [[n,n+1], [n+4,n+5], [n,n+4], [n+1,n+5]]) for n in [1,2,3,5,6,7,9,10,11]] + \
    [all([[n+i, n+j] in lines_list for i,j in [[0,1], [1, 2], [0, 4], [4,8], [8,9], [9,10], [2,6], [6,10]]]) for n in [1,2,5,6]] + \
    [all([i in lines_list for i in [[1,2], [2,3], [3,4], [4,8], [8,12], [12,16], [15,16], [14,15], [13,14], [9,13], [5,9], [1,5]]])])

if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"