class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def get_max_size(self):
        if self  is None:
            return 
        elif self.left is not None:
            
