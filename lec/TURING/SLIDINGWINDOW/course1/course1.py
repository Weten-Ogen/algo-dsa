# THE NAIVE SOLUTION 
def naiveaverage(nums,k=4):
    # set the maximum to negative infinity
    m = float("-inf")
    # loop through the array
    for i in range(len(nums)):
        # slide keeping track of the window
        window = 0
        # loop through the next 3  consecutive 
        for j in range(k):
            # if the current window has < 4 element
            if not (i + k- 1 > len(nums) - 1):
                # do the cumulative sum of the 4 nums
                window += nums[i + j] 
                # i + j so that you get the correct window

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