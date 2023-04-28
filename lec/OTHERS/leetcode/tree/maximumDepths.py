from Tree import Tree;
from collections import deque,defaultdict

def dfs(node):
    if not node:return
    d= deque([node])
    level = 0
    q = defaultdict(list)
     
    while d:
        for i in range(len(d)):
            node = d.popleft()
            q[level].append(node.value)
            if node.left:
                d.append(node.left)
            if node.right:
                d.append(node.right)
        level += 1
    return q.values()



n1 = [2,20,7,15]
tree = Tree(3)
tree.add_list(n1)

print(dfs(tree))