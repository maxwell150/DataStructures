"""
Coming up with the right solution to the linear search is the binary search which
improves on the time complexity
the logic to binary search is:
1. Find the middle element of the list
2. if it matches queried value, return the middle pos as answer
3. if it is less than the queried num, then search the first half of the list
4. if it is greater than the queried number then search the second half of the list
5. if no ore elements remain, return -1

"""


def find_value(lst, value):
    """to implement binary search the data has to be sorted either ascending or descending
    to ensure it sorted you can use the function sorted to sort the list ie sorted_list = sorted(list)
    """

    start = 0
    end = len(lst) - 1

    while start <= end:
        midpoint = (start + end) // 2
        mid_number = lst[midpoint]

        if mid_number == value:
            return midpoint

        elif mid_number < value:
            end = midpoint - 1

        elif mid_number > value:
            start = midpoint + 1
    return -1
