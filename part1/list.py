import sys
import array
a = ['marcus','gideon','oware', 'kofi','agyapong']
b = a[2:5]
print(b)
b[2] = 4
print(b)
print (a)
c = list(a)
c[0] = 9
# print(c)
# print(sys.getsizeof(a))
# print(sys.getsizeof(a[4]))
d = array.array('i',[1,2,3,4,5])
print(d)

