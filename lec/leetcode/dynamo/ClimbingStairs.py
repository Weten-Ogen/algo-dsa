# def climb(n):
#     one ,two = 1,1
#     for i in  range(n - 1):
#         temp = one
#         one  = one + two
#         two =  temp 
#     return one

def climb(n, memo={}):
    if n in memo : return memo[n]
    if n <= 1 : return 1 
    memo[n] =  climb(n-1) + climb(n - 2)
    return memo[n]



# examples 
print(climb(2))
print(climb(3)) 
print(climb(5))  
print(climb(16))      