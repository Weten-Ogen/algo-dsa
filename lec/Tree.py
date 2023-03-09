class Tree:
    def __init__(self,data, left=None, right=None) -> None:
        self.parent = data
        self.left = None
        self.right = None
    

    def insert(self, data):
        if self.parent == data:
            return False
        
        elif self.parent > data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = Tree(data)
                return
            
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = Tree(data)
                return
            
    def remove(self, data):
        if self.parent == data:
            if self.left is not None and self.right is not None:
                return 
            elif self.left:
                self.parent = self.left.parent
                self.left = None
                return 
            elif self.right:
                self.parent = self.right.parent
                return 
            else:
                self.parent = None
                return 
        elif self.parent > data:
            if self.left is None:
                return 
            else:
                self.left.remove(data)
        else:
            if self.right is  None:
                return 
            else:
                self.right.remove(data)


    def get_size(self):
            if self.left is not None and self.right is not None:
                return (1 + self.left.get_size() + self.right.get_size())
            elif self.left :
                return 1 + self.left.get_size()
            elif self.right:
                return 1 + self.right.get_size()
            else:
                return 1
    
    def preorder(self):
        if self is not None:
            print("PREORDER")
            print(self.parent, end='->')
            if self.left is not None :
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()

    def inorder(self):
        if self is not None:
            if self.left is not None :
                self.left.inorder()
            print("INORDER ")
            print(self.parent, end='->')
            if self.right is not None:
                self.right.inorder()
    
    def postorder(self):
        if self is not None:
            if self.left is not None :
                self.left.postorder()
            if self.right is not None:
                self.right.postorder()
            print("POST ORDER ")
            print(self.parent, end='->')
    
    
            

        
            

        
        
        
    def find(self, data):
        if self.parent == data:
            return data
        
        elif self.parent > data:
            if self.left is None:
                return False
            else:
                self.left.find(data)
        
        else:
            if self.right is  None:
                return False
            else:
                self.right.find(data)



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
tree.levelorder()
print()