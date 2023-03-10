# def containDup(arr):
#     arr = list(sorted(arr))
#     for i in arr:
#         for j in (arr[i:]):
#             if i != j :
#                 pass
#             else:
#                 return False

        
#     return True


# def containDup(arr):
#     dup = dict()
#     for j in arr:
#         if j not in dup:
#             dup[j] = 0
#         else:
#             return False
#     return True
     
def containDup(arr):
    dup = dict()
    for letter  in arr:
        if letter in dup:
            return False
        else:
            dup[letter] = 1
    return True
        




print(f"{containDup([1,2,3,1])}")
print(f"{containDup([1,2,3,4])}")
print(f"{containDup([1,1,1,3,3,4,3,2,4,2])}")