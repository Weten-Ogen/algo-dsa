def camSum(n,arr,memo= {}):
    if n in memo : return memo[n]
    if n == 0 :return True
    if n < 0:return False
    for num in arr:
        target = n - num
        if camSum(target,arr,memo) == True:
            memo[target] = True
            return True
    memo[n]=False
    return False

print(camSum(7,[2,3]))
print(camSum(7,[5,4,3,7]))
print(camSum(7,[2,4]))
print(camSum(300,[7,14]))
