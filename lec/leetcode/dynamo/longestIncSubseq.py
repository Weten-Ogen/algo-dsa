def longest(nums):
    ans = [1] * len(nums);
    for i  in range(len(nums)):
        for n in range(i):
            if nums[n] < nums[i]:
                ans[i] =max(ans[i],ans[n]+ 1)
    return max(ans)

# test 
print(longest([10,9,2,5,3,7,101,18]))
print(longest([0,1,0,3,2,3]))
print(longest([7,7,7,7,7,7,7,7]))
