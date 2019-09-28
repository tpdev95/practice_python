import random

a= random.sample(range(10), 6)

b=random.sample(range(10), 6)


c=[d for d in a if d in b]

# for e in b:
#     if e not in c:
#         c.append(e)

print(a)
print(b)
print(c)
