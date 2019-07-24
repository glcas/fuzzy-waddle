def str2int(s):
    try:
        s = int(s)
        return s
    except ValueError:
        s = input('请输入整数：')
        return str2int(s)


def input2D(m, n):
    """ 无权图 """
    data = [[0 for i in range(n)] for i in range(m)]  # use 'hard copy'
    for i in range(m):
        for j in range(n):
            if i == j:
                pass
            else:
                tempdata = str2int(
                    input('vector point%d->point%d: ' % (i + 1, j + 1)))
                while tempdata not in (0, 1):
                    tempdata = str2int(input('invalid relation!\n'))
                data[i][j] = tempdata
    return data


def main():
    m = str2int(input('how many points?\n'))
    tempList = input2D(m, m)
    for x in tempList:
        print(x)


if __name__ == "__main__":
    main()
