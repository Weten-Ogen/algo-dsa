def maxaverage(nums,k=4):
    windowSum = start = 0
    m = float("-inf")   
    for end in range(len(nums)):
        windowSum += nums[end]
        if end - start + 1 == k:
            m = max(m, windowSum/4)
            windowSum -= nums[start]
            start += 1
    return m




print(maxaverage([1,12,-5,-6,50,3]))