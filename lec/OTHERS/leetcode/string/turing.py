def rev(n):
    l=len(n)
    ans=list(n)
    for i in range(len(ans)):
        if   n[i] == ans[i] :
            if ans[i].isalpha():
                temp = ans[i]
                ans[i] = ans[l -1]
                ans[l-1] = temp 
                l-= 1
            else:
                ans[i] = n[i]
    return ''.join(ans)

# def rev(n):
#     ans=''
#     for i in n:
#         if not i.isalpha():
#             ans= i + ans
#         else:
#             ans = i + ans
#     return ans





# test 
print(rev('co-me'))
print(rev('ab-dc'))
print(rev('abase-ad'))
