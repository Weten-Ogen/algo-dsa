def subseq(n):
    anchor = ans = 0
    # loop through n
    for i in range(len(n)):
        # check if prev < curr
        if i > 0 and n[i-1] >= n[i]:
            anchor = i
        ans = max(ans, i - anchor + 1)

    # return ans
    return ans







# test 

n = [1,2,3,2,7] #return 3
m = [2,3,5,7,8] #return 5
print(subseq(n))
print(subseq(m))