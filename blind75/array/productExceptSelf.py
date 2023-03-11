def productExceptSelf(nums):
    product = 1
    n = len(nums) - 1
    def recursive_product(n):
        if n  == 0:
            return 
        else:
           product *= nums[n]
           return recursive_product(n - 1)
    return product




# Examples
# print(productExceptSelf([4,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))