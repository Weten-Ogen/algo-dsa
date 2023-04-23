a = [1,3,4,5]
t =5
def findcomp(a,t):
    for i in a:
        comp = t- i
        if comp in a:
            b = a.index(comp)
    return b
        

findcomp(a,t)