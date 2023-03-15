def  climb(n):
    accumulator = 0
    if n <= 0 : return 1
    if n - 1 < n : accumulator +=  climb(n - 1)
    if n - 2 < n : accumulator += climb(n - 2)
    return accumulator

print(climb(2))