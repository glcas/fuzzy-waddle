def str2float(s):
    try:
        s = float(s)
        return s
    except ValueError:
        s = input('请输入数字：')
        return str2float(s)


def errinList(temp, inList, i):
    while True:
        temp = str2float(input('请输入合适的数据：'))
        if temp >= inList[i - 1] and temp <= inList[0]:
            inList.append(temp)
            break


def getcircle():
    '''获取有序数据'''
    print('请输入成环数据，输入完成后按‘y’键')
    i, j = 0, 0
    inList = []
    while True:
        temp = input()
        if temp == 'y':
            break
        temp = str2float(temp)
        if i == 0:
            inList.append(temp)
        else:
            if temp < inList[i - 1]:  # 加判断j=1时最后值小于第一个
                j += 1
                if j > 1:
                    errinList(temp, inList, i)
            if j == 1:
                if temp <= inList[0]:
                    inList.append(temp)
                else:
                    errinList(temp, inList, i)
            if j == 0:
                inList.append(temp)
        i += 1
    return inList


def main():
    circle = getcircle()
    print(circle)


if __name__ == "__main__":
    main()
