from Tree import Tree


def sametree(p,q):
    if not p and not q:
        return True
    elif (not p and q) or (p and not q) or (p.value != q.value):
        return False
    return sametree(p.left,q.left) and sametree(p.right,q.right)
    return sametree(p,q)
        
def dfs(p,q ,s1=[],s2=[]):
    s1.append(p)
    s2.append(q)
    while len(s1) > 0:
        n1 = s1.pop()
        n2 = s2.pop()
        if not n1 and not n2:
            return True
        elif (not n1 and n2) or (n1 and not n2) or (n1.value != n2.value):
            return False
        return dfs(n1.left,n2.left) and dfs(n1.right,n2.right)
    return dfs(p,q)

            
        






p=Tree(1)
q=Tree(1)
p.add_list([2,5,4])
q.add_list([2,4,4])
print(sametree(p,q))
print(dfs(p,q))