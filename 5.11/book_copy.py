def next_permutation(perm):

    inversion_point = len(perm) - 2  # 2nd to last index
    while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]:
        inversion_point -= 1
    if inversion_point == -1:
        return []

    for i in reversed(range(inversion_point+1), len(perm)):
        if perm[i] > perm[inversion_point]

    print(inversion_point)


# perm = [6, 2, 1, 5, 4, 3, 0]
perm = [4,3,2,1,5]
next_permutation(perm)