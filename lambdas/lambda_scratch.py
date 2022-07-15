lst = [1,2,3,4,5]

z = lambda x: x %2 == 0

q = list(filter(z, lst))
