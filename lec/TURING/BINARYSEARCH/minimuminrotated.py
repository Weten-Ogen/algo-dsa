def rotated(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + right // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        elif nums[mid] > nums[mid + 1]:
            right = mid
    return nums[left + 1]



print(rotated([3,4,5,1,2]))
print(rotated([4,5,6,7,0,1,2]))