import random

d = []

for n in range(random.randint(1,10)):
    d.append(random.randint(1,10))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

c = [n for n in set(a) if n in d]
# for i in a:
#       if i in b and i not in c:
#           c.appen


print(c)
