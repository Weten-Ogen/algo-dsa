def robber(a):
    count =0
    for i in range(len(a)):
        if i % 2 == 0:
            count += a[i]
    return count
         





# test 
print(robber([1,2,3,4]))
print(robber([2,7,9,3,1]))