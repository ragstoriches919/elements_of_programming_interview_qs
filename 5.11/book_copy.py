def next_permutation(perm):

    inversion_point = len(perm) - 2  # 2nd to last index
    while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]:
        inversion_point -= 1
    if inversion_point == -1:
        return []

    print(inversion_point)
    print("\n")

    for i in reversed(range(inversion_point+1, len(perm))):

        print(perm[i], perm[inversion_point])

        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    print(perm)

    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    print(perm)
    #

    # perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    # return perm


def test(perm):

    for i in reversed(range(0, len(perm))):
        print(perm[i])


perm = [6, 2, 1, 5, 4, 3, 0]
# perm = [4, 3, 2, 1, 5]
# next_permutation(perm)
perm = list(reversed(perm[1:]))
print(perm)

# test(perm)