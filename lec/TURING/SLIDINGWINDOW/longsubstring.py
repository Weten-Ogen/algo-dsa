# def sub(n):
#     res=0
#     s = set()
#     for i in range(len(n)):
#             s.add(n[i])
#             res = max(res,len(s))
    
#     return res

def sub(n):
    res=0
    s=set()
    for letter in n:
        s.add(letter)
        res =max(res,len(s))
    return res
    
    



# test
print(sub('abcabcbb'))
print(sub('abcabcbb'))
print(sub('abcbcbb'))
print(sub('canyoudanco'))