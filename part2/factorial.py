def factoria(n):
    if n == 0:
        return 1
    else:
        return n * factoria(n - 1) 

print(factoria(5))