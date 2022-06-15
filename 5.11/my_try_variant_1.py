def next_smallest_variant(perm):

    inflection_point = len(perm) - 2

    while inflection_point >= 0 and perm[inflection_point] < perm[inflection_point + 1]:
        inflection_point -=1

    if inflection_point == -1:
        return perm

    # print(inflection_point)

    # for i in reversed(range(inflection_point + 1, len(perm))):
    for i in (range(inflection_point, len(perm))):
        if perm[i] < perm[inflection_point]:
            perm[i], perm[inflection_point] = perm[inflection_point], perm[i]

    print(perm)
    perm[inflection_point + 1:] = reversed(perm[inflection_point + 1 :])

    print(perm)

A = [6,2,1,5,3,4,7,8]

next_smallest_variant(A)