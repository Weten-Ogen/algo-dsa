def productExceptSelf(nums):
    ans = []
    for self in range(len(nums)-1):
            other = nums[:]
            product = 1
            other.pop(self)
            for mul in other:
                product *= abs(mul)
            ans.append(product)
    return ans

    # get the self
    # get all the value of the others
    # compute their product
    # return their product

       






# Examples
print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,1,-3,3]))