# def productExceptSelf(nums):
#     left = [1] * len(nums)
#     for  i in range(1,len(nums)):
#         left[i] = left[i-1]*nums[i-1]

#     right = [1] * len(nums)
#     for i in range(len(nums)-2,-1,-1):
#         right[i] = right[i+1]*nums[i+1]

#     ans = [0] * len(nums)
#     for i in range(len(nums)):
#         ans[i] = left[i]*right[i]

#     return ans


   
def productExceptSelf(nums):
    ans = [1] * len(nums)
    for i in range(1,len(nums)):
        ans[i] = nums[i] * nums[i-1]
   
    product = 1
    ans[len(nums)-1] = ans[len(nums)-2]
    for i in range (len(nums)-1, 0,-1):
        product *= nums[i]
        ans[i-1] = ans[i-2] * product
    ans[0] = product
    return ans

        
 


# # Examples
print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))