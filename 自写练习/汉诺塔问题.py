def hanoi(n, a, b, c):
    if n == 1:
        print('1:{}->{}'.format(a, c))
        return
    hanoi(n - 1, a, c, b)
    print('{}:{}->{}'.format(n, a, c))
    hanoi(n - 1, b, a, c)


n = int(input('how many?'))
hanoi(n, 'A', 'B', 'C')
