def next_permutation(A):
    sub = []
    increasing = True
    replace_val = None
    replace_idx = None
    replace_idx_other = None

    for i in range(0, len(A[::-1])):

        if i == 0:
            sub.append(A[::-1][i])
        elif (A[::-1][i] > A[::-1][i - 1]) and increasing:
            sub.append(A[::-1][i])
        elif increasing:
            increasing = False
            replace_val = A[::-1][i]
            replace_idx = i

    for i in range(1, len(sub)):
        if replace_val >= sub[i - 1] and replace_val <= sub[i]:
            replace_idx_other = i

    # A[::-1][replace_idx], A[::-1][replace_idx_other] =  A[::-1][replace_idx_other], A[::-1][replace_idx]

    A[-1 * (replace_idx) - 1], A[-1 * (replace_idx_other) - 1] = A[-1 * (replace_idx_other) - 1], A[
        -1 * (replace_idx) - 1]

    new_sub = list(reversed(A[replace_idx - 1:]))  # .reverse()
    new_pre = A[:replace_idx - 1]

    final = new_pre + new_sub

    print(final)

    return final


arr = [6, 2, 1, 5, 4, 3, 0]
# arr = [1,2,3,4]
# arr = [4,3,2,1]

next_permutation(arr)

