from Tree import Tree

def invert(node):
    if not node:
        return None
    invert(node.left)
    invert(node.right)
    node.left,node.right = node.right,node.left
    print(node.value)
    return node
   

t= Tree(3)
t.add_list([9,20,15,7])


invert(t)

def dfs(t):
    if not t:
        return None
    dfs(t.left)
    dfs(t.right)
    print(t.value)

