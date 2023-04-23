def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        for j in range(i-1,0,-1):
            if arr[j] > current:
                arr[j + 1] = arr[j]
            else:
                arr[j + 1] = current
                break;
    return arr

arr=[7,8,9,0,4,3]

print(insertionSort(arr))