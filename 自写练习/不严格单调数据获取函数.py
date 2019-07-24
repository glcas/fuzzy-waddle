def getData():
    '''输入线性数据'''
    print('请输入数据，输入完成后按‘y’键')
    i, j, con = 0, 0, None
    tempList = []
    while True:
        temp = input()
        if temp == 'y':
            break
        temp = str2float(temp)
        if i == 0:
            tempList.append(temp)
        if i >= 1:
            if j == 0:
                if temp > tempList[i - 1]:
                    con = '>'
                    j += 1
                if temp < tempList[i - 1]:
                    con = '<'
                    j += 1
            if con == '>':
                while True:
                    if temp >= tempList[i - 1]:
                        tempList.append(temp)
                        break
                    temp = input('数据 {} 无效！请输入更大的数据（或输入‘y’结束输入）：'.format(temp))
                    if temp == 'y':
                        con = -1
                        break
                    temp = str2float(temp)
            if con == '<':
                while True:
                    if temp <= tempList[i - 1]:
                        tempList.append(temp)
                        break
                    temp = input('数据 {} 无效！请输入更小的数据（或输入‘y’结束输入）：'.format(temp))
                    if temp == 'y':
                        con = -1
                        break
                    temp = str2float(temp)
            if con is None:
                tempList.append(temp)
            if con == -1:
                break
        i += 1
    return tempList

