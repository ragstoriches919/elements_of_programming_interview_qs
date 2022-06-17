import random

def random_sampling(A, k):
    print(A)
    for i in range(k):
        random_value = random.randint(i, len(A) - 1)
        A[i], A[random_value] = A[random_value], A[i]

    print(A)

A = [1,2,3]
k = 2

random_sampling(A, k)