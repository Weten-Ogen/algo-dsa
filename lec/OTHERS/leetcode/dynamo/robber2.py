def robber(n):
    count=0
    for i in range(len(n)):
        if i % 2 !=  0:
            count += n[i]
    return count



# test
print(robber([2,3,2])) 
print(robber([1,2,3,1])) 