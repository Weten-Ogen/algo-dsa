# immutable
# useful for fixed data
# faster than list
# sequence types


# constructor
x = ()
y = 3,

# print(type(x))
# print(type(y))

# tuples are immutable but member data which are mutable can be changed

m = [1,2,3]
f = m,23
del(f[0][2])
# print(f)

