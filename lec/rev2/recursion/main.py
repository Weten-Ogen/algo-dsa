# def getPosition(l):
#     # base case 
#     # if the the array is empty
#     # return 0
#     n = len(l)
#     if n  ==  0: return 0
#     return 1 + getPosition(l[1:])


# # tests
# l = [1,2,3,4,5,6,7,8,9,11]
# print(getPosition(l))

# String Reversal

# def str_reverse(s):
#    if len(s) <= 1: return s[0]
#    return  str_reverse(s[1:]) + s[0]


# def str_palindrom(s):
#     if s[0] == s[len(s) - 1] : 
#         return True
#     if s[0] == s[len(s) -1]: 
#         return str_palindrom(s[0:len(s)-1])
#     return False


def decimal_binary(n, num=''):
   
    if n == 0 : return num
    num =str( n % 2) + num
    return decimal_binary(n//2,num)


# test case
print(decimal_binary(233))
print(decimal_binary(58))
print(decimal_binary(23))
print(decimal_binary(64))

