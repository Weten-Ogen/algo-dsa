# def common(t1,t2):
#    count = 0
#    for i in t2:
#       if i in t1:
#          count += 1
#    return count
         
def common(t1,t2,count=0):
    if len(t1) == 0 or len(t2) == 0: return count
    if t2[0] in t1: count += 1 
    return common(t1,t2[1:], count)


print(common('abc','abcde'))
print(common('abc','abc'))