string = "I needed practice, so I used this list. Each challenge below links to a solution gist."
x = [i for i in range(1, 1001) if i%7==0]

x = [i for i in range(1, 1001) if "3" in str(i)]



x = "".join([i for i in string if i.lower() not in ["a", "e", "i", "o", "u"]])

rando = ['hi', 4, 8.99, 'apple', ('t,b', 'n')]
x = [ (i, rando[i]) for i in range(0, len(rando)) ]

list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2,7,1,12]

x = [i for i in list_a if i in list_b]

sentence = "In 1984 there were 13 instances of a protest with over 1000 people attending"
x = [i for i in sentence.split(" ") if i.isnumeric() ]


x =['even' if n%2==0 else'odd' for n in range(20)]

x = [(i,i) for i in list_a if i in list_b]

x = [i for i in sentence.split(" ") if len(i) <4 ]

# print(x)

# matrix = [[j for j in range(5)] for i in range(3)]
# matrix = [[j for j in range(2)] for i in range(3)]
# print(matrix)

table = [["hi" for row in range(10)] for col in range(10) ]
print(table)




# print(int("str"))

