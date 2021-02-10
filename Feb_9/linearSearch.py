def linearSearch(lst, elem):
    '''
        Return the index of `elem` in `lst` (if exists).
        If not in `lst`, return -1
    '''

    for i in range(len(lst)):
        if lst[i] == elem:
            print(':)')
            return i

    print(':(')
    return -1

if __name__ == '__main__':
    myList = [10, 3, 2, 3, 8, 99, 100, 15, 16]
    # elem = 99
    elem = 3
    print('The position of', elem, 'is', linearSearch(myList, elem))