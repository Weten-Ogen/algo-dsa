# constructor
x = list()

# appending
x.append(50)
x.append(100)

# deleting
del(x[-1:])

# extending
y = [1,2,3]

x.extend(y)

# inserting
k= [-1,2,-3]
x.insert(3,k)

# poping
x.pop()

# removing
x.remove(k)

# reverse
x.reverse()
# print(x)
# print(list(reversed(k)))
# print(k)

# sort
k.sort(reverse=True)
# print(k)
y = list(sorted(x))

# print(y)


"""List Comprehension"""
import random

# getting range
under_10 = [x for x in range(10)]
print(f"under_10: {under_10}")

# getting squared 
square = [x**2 for x in range(1,10)]
print(f"square: {square}")

# getting old numbers
odd = [x for x in range(10) if x%2 != 0]
print(f"odd: {odd}")

# getting all number from string
s = "I love 2 to g0 t0 the store 7 times a w3ek."
numbs = [x for x in s if x.isnumeric()]
print(f"numbs: {''.join(numbs)}")