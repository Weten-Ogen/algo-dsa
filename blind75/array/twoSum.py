# def twosum(nums,target):
#     ans = list()
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 ans.append(i)
#                 ans.append(j)
#                 return ans  
#             else:
                # continue

# def twosum(nums, target):
#     obj = {}
#     for i , n in enumerate(nums):
#         obj[n] = i

#     for k in obj.keys():
#         m = target - k
#         if m >= 0 and k != m:
#             if m  in obj.keys():
#                 return [obj[k],obj[m]]
#             else:
#                 continue
#         else:
#             continue
            
        
def twosum(nums,target):
    complementMap = dict()
    for i in range(len(nums)):
        num = nums[i]
        comp = target - num # 9 - 0
        if num in complementMap: # 0
            return [complementMap[num], i]
        else:
            complementMap[comp] = i
    return -1







# Examples

print(twosum([2,7,11,15],9))
print(twosum([3,2,4],6))