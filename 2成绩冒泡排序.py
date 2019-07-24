def str2int(s):
    try:
        s = int(s)
        return s
    except ValueError:
        s = input('请输入整数：')
        return str2int(s)


def str2float(s):
    try:
        s = float(s)
        return s
    except ValueError:
        s = input('请输入整数：')
        return str2float(s)


def main():
    n = input('请输入学生人数：')
    n = str2int(n)
    while True:
        if n < 1:
            n = str2int(input('请输入正数：'))
        else:
            break
    stu = [[] for i in range(n)]
    for i in range(n):
        stu[i] = input('请输入第{}个学生的姓名和成绩（以空格分隔）：'.format(i + 1)).split()
        while True:
            if stu[i] == []:
                stu[i] = input('请输入内容！\n').split()
            else:
                break
        while True:
            try:
                stu[i][1] = str2float(stu[i][1])
                break
            except IndexError:
                stu[i].append(input('请输入成绩：'))
        while True:
            if stu[i][1] > 100 or stu[i][1] < 0:
                stu[i][1] = str2float(input('成绩的范围在0~100之间：'))
            else:
                break
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if stu[j][1] <= stu[j + 1][1]:
                t = stu[j]
                stu[j] = stu[j + 1]
                stu[j + 1] = t
    k = input('想要打印前多少名的成绩？\n')
    k = str2int(k)
    while True:
        if k > n:
            k = str2int(input('数值应小于学生人数！\n'))
        elif k < 1:
            k = str2int(input('请输入正数：'))
        else:
            break
    i = 0
    while (k >= 1):
        print('第{}名：{}，{}分'.format(i + 1, stu[i][0], stu[i][1]))
        k -= 1
        i += 1
    input('Enter any keys to exit...')


if __name__ == '__main__':
    main()
