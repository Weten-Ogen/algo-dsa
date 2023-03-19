def maxiSub(nums):
    # accum -> reset when < 0
    ans = 0
    s = 0
    for num in nums:
        if s < 0:
            s = 0
        s += num
        if s > ans:
            ans = s
        
    return ans





print(maxiSub([-2,1,-3,4,-1,2,1,-5,4]))
print(maxiSub([5,4,-1,7,8]))
print(maxiSub([-2,0,-1]))


