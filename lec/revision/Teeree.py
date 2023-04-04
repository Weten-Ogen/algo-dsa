
class Tree:
    def __init__(self,data,left=None,right=None):
        self.node = data
        self.left = left
        self.right= right


    def insert(self,val):
        if self.node == val:
            return False
        elif  self.node > val:
            return self.insert(self.node.left,val)
        else:
            return self.insert(self.node.right,val)
       

    def travers(self):
        if self is not None:
            if self.left is not None:
                self.left.travers()
            print(self.node , end=" ")
            if self.right is not None:
                self.left.travers()
        print()
                





t = Tree()
t.insert(5)
t.insert(3)
t.travers()
