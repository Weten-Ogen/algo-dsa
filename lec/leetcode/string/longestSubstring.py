# def sub(n):
#     arr = []
#     for i in range(1,len(n)):
#         if n[i] != n[i- 1]:
#             arr.append(n[i])
#     if n == '':
#         return 0
#     if len(arr) == 0:
#         return 1
#     return len(set(arr))

def sub(n):
    charSet = set()
    l = 0
    ans = 0
    for r in range(len(n)):
        while n[r] in charSet:
            charSet.remove(n[l])
            l += 1
        charSet.add(n[r])
        ans = max(ans,r - l + 1)
    return ans

# test
print(sub('abcabcbb'))
print(sub('bbbb'))
print(sub('pwwkew'))
print(sub('marcus'))
print(sub(''))