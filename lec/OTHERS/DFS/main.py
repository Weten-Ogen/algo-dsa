class Node: 
    def __init__(self,value, left=None,right=None):
        self.value = value 
        self.left = left
        self.right = right

    def __str__(self):
        return "Node(" + str(self.value) + ")"
    

def dfs(tree):
    if tree is not None:
        dfs(tree.left)
        print(tree)
        dfs(tree.right)

def stackdfs(tree,stack=[]):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            stack.append(node.right)
            print(node)
            stack.append(node.left)


# test
mytree = Node('A', Node('B',Node('D'),Node('E')),Node('C',Node('F'),Node('G')))

dfs(mytree)