import random
def random_sampling(k, A):
    for i in range(k):
        r = random.randint(i, len(A)-1)
        A[i], A[r] = A[r], A[i]

    print(A)


A = [1,2,3]
random_sampling(2, A)
