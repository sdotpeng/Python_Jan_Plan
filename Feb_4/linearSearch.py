'''linearSearch.py
First algorithm you would learn!
'''

def linearSearch(lst, search_element):
    '''
    Implementation of Linear Search, return the index of the `search_element`
    if not found, return -1

    Input:
        lst: list, the original list
        search_element: int, a number to be searched for
    Return:
        int, the index of the `search_element` in the `lst`
    '''
    # for i in lst:
    #     if i == search_element:
    #         return lst.index(i)
    #     else:
    #         return -1

    for i in range(len(lst)):
        if lst[i] == search_element:
            return i
    return -1

lst = [3,4,7,9,10]
search_element = 7
print(linearSearch(lst, search_element))

