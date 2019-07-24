def input2D(m, n):
    data = [[0 for i in range(n)] for i in range(m)]  # use 'hard copy'
    for i in range(m):
        for j in range(n):
            data[i][j] = int(input())
    return data


def main():
    m, n = map(int, input('row and col:').split())
    tempList = input2D(m, n)
    print(tempList)
    return


if __name__ == "__main__":
    main()
