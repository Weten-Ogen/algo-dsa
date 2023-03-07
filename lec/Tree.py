class Tree:
    def __init__(self, parent , left=None,right=None):
        self.parent = parent 
        self.left = left
        self.right= right

    def insert(self,data):
        if self.parent == data:
            # this is to avoid duplicates
            return False
            
        elif self.parent > data:
            # loop through the leftside 
            if self.left is not None:
                return self.left.insert(data);
            # if empty create a subtree
            else:
                self.left = Tree(data)
                return True
            
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right= Tree(data)
                return True
            
    def find(self, data):
        if self.parent == data:
            return data
        elif self.parent > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.parent < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)
            
    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        if self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1 
        
    def preorder(self):
        if self.parent is not None:
            print(self.parent , end=' ')
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()

    def inorder(self):
        if self.parent is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.parent, end=' ')
            if self.right is not None:
                self.right.inorder()
    
    def postorder(self):
        if self.parent is not None:
            if self.left is not None:
                self.left.postorder()
            if self.right is not None:
                self.right.postorder()
            print(self.parent,end=' ')
    

tree = Tree(7)
tree.insert(9)
for i in [15,10,2,12,3,1,13,6,11,4,14,9]:
    tree.insert(i)
for i in range(16):
    print(tree.find(i), end=' ')
print('\n', tree.get_size())
tree.preorder()
print()
tree.postorder()
print()
tree.inorder()
print()