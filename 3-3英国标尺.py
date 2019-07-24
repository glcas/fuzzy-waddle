def str2int(s):
    try:
        s = int(s)
        return s
    except ValueError:
        s = input('Please enter an integer:')
        return str2int(s)


def drawruler(num, lenth):
    print('-' * lenth + ' 0')
    for i in range(num):
        drawinit(lenth - 1)
        print('-' * lenth + ' {}'.format(i + 1))


def drawinit(n):
    if n == 0:
        return
    else:
        drawinit(n - 1)
        print('-' * n)
        drawinit(n - 1)


def main():
    num = str2int(input('num:'))
    lenth = str2int(input('lenth:'))
    drawruler(num, lenth)


if __name__ == "__main__":
    main()
