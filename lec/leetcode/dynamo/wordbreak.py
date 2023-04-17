def workbreak(n, arr):
    m = ''
    for i in arr:
        m += i
    for i in m:
        if i not in n:
            return False
    return True
    



# tesgt
print(workbreak('leetcode' , ['leet','code']))
print(workbreak('applepenapple',['apple','pen']))

