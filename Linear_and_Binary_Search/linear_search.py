"""Implementing a linear search algorithm
The search happens sequentially that is from left->right or vice versa
Each value is checked against the query meaning the worst time complexity for this algotithm is O(n)
such that as data increases so is the time required for a search
"""

def find_value(lst, value):
    # setting the initial index from where to start the search
    pos = 0

    print(f'LIST: {lst}\nQUERY: {value}')

    # setup a while loop to loop through each value in the list and ensuring the query is not out of range
    while pos < len(lst):
        # compare
        if lst[pos] == value:
            return pos
        pos = pos + 1

    # when value is not in list
    return -1
