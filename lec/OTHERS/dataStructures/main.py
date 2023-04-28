class Tree: 
  
    def __init__(node, value): 
        node.value = value  
        node.left = None
        node.right = None
    
    def Inorder( node, Root ): 
        if( Root is None ): 
            return
        node.Inorder(Root.left) 
        print(Root.value,end = ' ') 
        node.Inorder(Root.right) 
  
    def Insert(node, value): 
        if node is None: 
            node = Tree(value)
        elif value < node.value:
            if node.left is None:
                node.left = Tree(value)
            else:
               node.left.Insert(value) 
        else:
            if node.right is None:
                node.right = Tree(value)
            else:
                node.right.Insert(value)
Root = Tree(6) 
Root.Insert(4) 
Root.Insert(2) 
Root.Insert(5) 
Root.Insert(9) 
Root.Insert(8) 
Root.Insert( 10) 

print ("Inorder traversal after insertion: ",end = '')
Root.Inorder(Root)
