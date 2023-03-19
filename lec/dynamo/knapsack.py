def knapsac(arr, target):
    for i in arr:
        for j in arr:
            if i + j == target:
                return True
    return False

print(knapsac([3,5,2,7,9],10))
print(knapsac([2,4,6],11))