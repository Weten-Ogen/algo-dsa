# THE NAIVE SOLUTION 
def naiveaverage(nums,k=4):
    m = float("-inf")
    for i in range(len(nums)):
        window = 0
        for j in range(k):
            if not (i + k- 1 > len(nums) - 1):
                window += nums[i + j] 
            else:
                i = len(nums)
                j = k
        if window != 0:
            m = max(m,window/4)
    if m == float('-inf'):
        return 0
    return m





# test
print(naiveaverage([1,12,-5,-6,50,3]))