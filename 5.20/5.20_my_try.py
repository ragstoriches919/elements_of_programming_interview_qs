# IT WORKS!! IT FUCKING WORKS!!!

def pascal(n):

    arr = []

    for i in range(n):
        temp = []
        for j in range(len(arr)+1):
            temp.append(1 if j ==0 or j == len(arr) else arr[i-1][j-1] + arr[i-1][j])
        arr.append(temp)
        print(temp)

    print(arr)

pascal(6)