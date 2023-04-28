def bucket_sort(arr):
    a = {}
    for num in arr:
        if num in a:
            a[num] += 1
        else:
            a[num] = 1
    return a


arr = [1,1,1,2,2,3]

print(bucket_sort(arr))