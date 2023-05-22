import random
t = random.randint(1, 100)
a = [i for i in range(1, t)]
b = []
for i in range(1, t):
    a.append(random.randint(1, 100))
    b.append(random.randint(1, 100))

newlist = list(set([i for i in a if i in b]))
print(newlist)