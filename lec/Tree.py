class Tree:
    def __init__(node,data, left=None, right=None):
        node.value = data
        node.left = None
        node.right = None

    def insert(node, data):
        if node.value == data:
            return False

        elif node.value > data:
            if node.left is not None:
                node.left.insert(data)
            else:
                node.left = Tree(data)
                return

        else:
            if node.right is not None:
                node.right.insert(data)
            else:
                node.right = Tree(data)
                return
            



    def get_size(node):
            if node.left is not None and node.right is not None:
                return (1 + node.left.get_size() + node.right.get_size())
            elif node.left :
                return 1 + node.left.get_size()
            elif node.right:
                return 1 + node.right.get_size()
            else:
                return 1
    
    def preorder(node):
        if node is not None:
            print("PREORDER")
            print(node.value, end='->')
            if node.left is not None :
                node.left.preorder()
            if node.right is not None:
                node.right.preorder()

    def inorder(node):
        if node is not None:
            if node.left is not None :
                node.left.inorder()
            print("INORDER ")
            print(node.value, end='->')
            if node.right is not None:
                node.right.inorder()
    
    def postorder(node):
        if node is not None:
            if node.left is not None :
                node.left.postorder()
            if node.right is not None:
                node.right.postorder()
            print("POST ORDER ")
            print(node.value, end='->')

        
    def find(node, data):
        if node.value == data:
            return data 
        
        elif node.value > data:
            if node.left is None:
                return False
            else:
                node.left.find(data)
        
        else:
            if node.right is  None:
                return False
            else:
                node.right.find(data)



tree = Tree(7)
tree.insert(9)
for i in [15,10,2,12,3,1,13,6,11,4,14,9]:
    tree.insert(i)
# for i in range(16):
#     print(tree.find(i), end=' ')
# print('\n', tree.get_size())
tree.preorder()
print()
print()
tree.postorder()
print()
print()
tree.inorder()
print()
print()
