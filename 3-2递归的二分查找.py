def bsearch(list0, x):
    """ return the position in the list, or -1 """
    low, high, mid = 0, len(list0) - 1, len(list0) // 2
    return inbsearch(list0, x, low, high, mid)


def inbsearch(list0, x, low, high, mid):
    if list0[mid] != int(x):
        if mid in (low, high):
            return -1
        elif int(x) < list0[mid]:
            high = mid - 1
            mid = (low + high) // 2
            return inbsearch(list0, x, low, high, mid)
        else:
            low = mid + 1
            mid = (low + high) // 2
            return inbsearch(list0, x, low, high, mid)
    return mid


def main():
    """ test part """
    testList = [i for i in range(10)]
    print('the test list is: {}'.format(testList))
    print('find 3, the position are: {}.'.format(bsearch(testList, 3)))
    print("find 11 which is not in the list, return {}.".format(bsearch(testList, 11)))


if __name__ == "__main__":
    main()
"""
Output:
the test list is: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
find 3, the position are: 3.
find 11 which is not in the list, return -1.
"""
