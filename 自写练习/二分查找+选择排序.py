def bsearch(list):
    list.sort()
    low, high, mid = 0, len(list) - 1, len(list) // 2
    x = input('Enter the number:')
    while list[mid] != int(x):
        if mid == (low or high):
            return -1
        elif int(x) < list[mid]:
            high = mid - 1
            mid = (low + high) // 2
        else:
            low = mid + 1
            mid = (low + high) // 2
    return mid


list = [23, 65, 897, 45, 87, 4, 53, 435, 7, 2, 553, 345, 76]
print(sorted(list, reverse=True))
for i in range(len(list)):
    max_ = i
    for j in range(i + 1, len(list)):
        if list[max_] < list[j]:
            max_ = j
    list[max_], list[i] = list[i], list[max_]
print(list)
position = bsearch(list)
if position == -1:
    print('out of rage')
else:
    print('是第{}小的数'.format(position + 1))
'''
#递归的二分查找
def bsearch(list0, x):
    low, high, mid = 0, len(list0) - 1, len(list0) // 2
    return inbsearch(list0, x, low, high, mid)


def inbsearch(list0, x, low, high, mid):
    if list0[mid] != int(x):
        if mid == (low or high):
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
'''
