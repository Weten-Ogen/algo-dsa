def twosum(n,t):
    res = []
    # loop through n
    for i,num in enumerate(n):
        comp = t - num
        if comp != num and len(res) <= 2 and comp in n :
                if n.index(comp) not in res:
                    res.append(n.index(comp))
                    res.append(i)
    return res





# test
print(twosum([2,7,11,15],9))
print(twosum([3,2,4],6))
print(twosum([2,7,11,15],0))
