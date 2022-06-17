import itertools
import random


def online_random_sample(stream, k):
    running_sample = list(itertools.islice(stream, k))
    print(running_sample)

stream = ["A",2,3,4,5]
k=2
online_random_sample(stream, k)

print(list(itertools.islice(stream, k)))


# x = itertools.chain("AC", "DE", "GHI2")
# print(list(x))

