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


num, lenth = input('num and lenth:').split()
drawruler(int(num), int(lenth))
