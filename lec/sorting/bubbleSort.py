
def bubbleSort(arr):
    
    for i in range(len(arr)):
       j = i + 1
       for m in range(j, len(arr)-1-i):
            if arr[i] > arr[m]:
                arr[i], arr[m] = arr[m], arr[i]
    return arr


print(bubbleSort([3,2,1,4,6,7]))