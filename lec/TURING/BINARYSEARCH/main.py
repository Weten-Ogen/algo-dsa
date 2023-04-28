def b_search(arr):
    left = 0
    right= len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left =  mid + 1
        if arr[mid] > arr[mid + 1]:
            right = mid
    return left




print(b_search([ 24,64,100,90,79,78,67,36,26,19]))
print(b_search([4,5,6,7,0,1,2]))