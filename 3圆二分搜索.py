import random


def str2float(s):
    try:
        s = float(s)
        return s
    except ValueError:
        s = input('请输入数字：')
        return str2float(s)


def str2int(s):
    try:
        s = int(s)
        return s
    except ValueError:
        s = input('请输入整数：')
        return str2int(s)


def str2floatp(s):
    '''返回的第二个值给brk'''
    try:
        s = float(s)
        return s, 0
    except ValueError:
        if s == 'y':
            return None, 1
        else:
            s = input('请输入数字或‘y’：')
            return str2floatp(s)


def getData():
    '''输入线性数据'''
    print('请输入严格单调的数据，输入完成后按‘y’键')
    i, brk = 0, 0
    tempList = []
    while True:
        if i == 0:
            temp = str2float(input())
            tempList.append(temp)
        if i == 1:
            temp = str2float(input())
            while True:
                if temp != tempList[0]:
                    if temp > tempList[0]:
                        con = 'increase'
                        tempList.append(temp)
                    else:
                        con = 'decline'
                        tempList.append(temp)
                    break
                else:
                    temp = str2float(input('请输入不相等的数据：'))
        if i > 1:
            temp, brk = str2floatp(input())
            if brk == 1:
                break
            if con == 'increase':
                while True:
                    if temp > tempList[i - 1]:
                        tempList.append(temp)
                        break
                    else:
                        temp, brk = str2floatp(
                            input(
                                '数据 {} 无效！请输入更大的数据（或输入‘y’结束输入）：'.format(temp)))
                    if brk == 1:
                        break
            if con == 'decline':
                while True:
                    if temp < tempList[i - 1]:
                        tempList.append(temp)
                        break
                    else:
                        temp, brk = str2floatp(
                            input(
                                '数据 {} 无效！请输入更小的数据（或输入‘y’结束输入）：'.format(temp)))
                    if brk == 1:
                        break
            if brk == 1:
                break
        i += 1
    return tempList, con


def getCircle(tempList):
    '''有序数据成环'''
    i = random.randint(0, len(tempList) - 1)
    inList = [0] * len(tempList)
    for x in tempList:
        inList[i] = x
        i = (i + 1) % len(tempList)
    return inList


def searchMin(circle):
    low, high = 0, len(circle) - 1
    mid = (low + high) // 2
    while mid != low:
        if circle[low] < circle[high]:
            if circle[mid] > circle[low]:
                if circle[mid] < circle[high]:  # min mid max
                    return low
                else:  # min max mid
                    high = mid
                    mid = (low + high) // 2
            else:  # mid min max
                low = mid
                mid = (low + high) // 2
        elif circle[low] > circle[high]:
            if circle[mid] > circle[high]:
                if circle[mid] < circle[low]:  # max mid min
                    return high
                else:  # mid max min
                    low = mid
                    mid = (low + high) // 2
            else:  # max min mid
                high = mid
                mid = (low + high) // 2
    if circle[mid] > circle[high]:
        return high
    else:
        return mid


def bsearch(x, List, con):
    '''二分查找'''
    low, high, mid = 0, len(List) - 1, len(List) // 2
    if con == 'increase':
        while List[mid] != x:
            if mid == low:
                if List[high] == x:
                    mid = high
                else:
                    return -1
            elif x < List[mid]:
                high = mid
                mid = (low + high) // 2
            else:
                low = mid
                mid = (low + high) // 2
    else:
        while List[mid] != x:
            if mid == low:
                if List[high] == x:
                    mid = high
                else:
                    return -1
            elif x > List[mid]:
                high = mid
                mid = (low + high) // 2
            else:
                low = mid
                mid = (low + high) // 2
    return mid


def find(x, circle, positionMin, con, k=0):
    if con == 'increase':
        if k >= positionMin:
            temposition = bsearch(x, circle[k:], con)
            if temposition == -1:
                position = -1
            else:
                position = temposition + k
        else:
            position1 = bsearch(x, circle[k:positionMin], con)
            position2 = bsearch(x, circle[positionMin:], con)
            if position1 != -1:
                position = position1 + k
            elif position2 != -1:
                position = position2 + positionMin
            else:
                position = -1
    else:
        if k > positionMin:
            temposition = bsearch(x, circle[k:], con)
            if temposition == -1:
                position = -1
            else:
                position = temposition + k
        else:
            position1 = bsearch(x, circle[k:positionMin + 1], con)
            position2 = bsearch(x, circle[positionMin + 1:], con)
            if position1 != -1:
                position = position1 + k
            elif position2 != -1:
                position = position2 + positionMin + 1
            else:
                position = -1
    return position


def searchk(circle, con, positionMin):
    '''从k位置开始查找数据'''
    x = str2float(input('请输入想要查找的数据：'))
    k = str2int(input('请输入查找范围的起始位置（1~{}之间）：'.format(len(circle))))
    while k < 1 or k > len(circle):
        k = str2int(input('请输入合适的起始位置！'))
    positionx = find(x, circle, positionMin, con, k - 1) + 1
    if positionx == 0:
        print('数据{}不在查找范围{}当中！'.format(x, circle[k - 1:]))
    else:
        print('数据{}在{}中的第{}位（{}中的第{}位）。'.format(
            x, circle, positionx, circle[k - 1:], positionx - k + 1))


def main():
    data, con0 = getData()
    circle0 = getCircle(data)
    positionMin = searchMin(circle0)  # 从0开始的
    searchk(circle0, con0, positionMin)
    while True:
        c = input('想要继续查找吗？（y/n）\n')
        if c == 'y':
            searchk(circle0, con0, positionMin)
        elif c == 'n':
            break
    input('Enter any keys to exit...')


if __name__ == "__main__":
    main()
