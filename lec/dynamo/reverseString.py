# def rever(string):
    
#     if len(string) == 0:return  ""
    
   
#     return rever(string[1:]) + string[0]
    

# print(rever("hello"))

def add(nums):
    if len(nums) == 0:
        return 0
    return add(nums[1:]) + nums[0]

print(add([1,2,3,4,5,6,7,7,8,89,7,8,9,7,8,9,8,7,8,77,8,8,77,7,6,7,6,7,6,6,6,6,7,65,6,55,6,7,5,7,5,6,7,5,6,76]))