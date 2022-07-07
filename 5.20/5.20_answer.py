def pascal(n):
    arr = [[1] * i for i in range(1, n+1)]
    print(arr)

    for i in range(n):
        for j in range(1, i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(arr)

pascal(6)