from Tree import Tree
from collections import defaultdict

def level(node):
    d = defaultdict(list)
    def bfs(node,c=0):
        if not node:return
        d[c].append(node.value)
        c += 1
        bfs(node.left,c+1)
        bfs(node.right,c+1)
            
    bfs(node)
    return d.values()
    

    




t= Tree(3)
t.add_list([2,20,15,7])
print(level(t))
