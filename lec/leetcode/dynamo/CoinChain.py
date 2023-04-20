def coins(nums,t,ans=0):
    if len(nums) <  0 : return -1
    if len(nums) == 1 and nums[0] < t: return -1

    return coins(nums[1:],t,ans)


print(type(float('inf')))
# test 
# print(coins([1,2,5],11))
# print(coins([2], 3))
# print(coins([1],0))