def binar(n , result= ""):
    if n == 0 : 
        return result
    result = str(n % 2)  + result;
    return binar(n // 2, result)

print(binar(504340450509550))