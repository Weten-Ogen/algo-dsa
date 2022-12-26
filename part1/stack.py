# class LinkList:

#     class _Node:
#         def __init__(self, e , next):
#             self.element = e
#             self.next = next

#         def __str__(self):
#             return f"{self.element}, {self.next}"

#     def __init__(self):
#         self.head = None
#         self.size = 0

#     def size(self):
#         return self.size

#     def is_empty(self):
#         return self.size  == 0
    
#     def push(self, e):
#         current = self.head.element
#         self.head = self._Node(e, self.head)
#         self.head.next = current
#         self.size += 1
        

#     def first(self):
#         return self.head.element
    





class mystack: 
    def __init__(self):
        self.arr = []

    def __str__(self):
        return f"{self.arr}"
    
    def is_empty(self):
        return len(self.arr) == 0
    

    def  push(self,e):
        self.arr.append(e)
        
   
    def size(self):
        return len(self.arr)
    
    def pop(self):
        if self.is_empty():
            return 
        else:
            return self.arr.pop()




m = mystack()
m.push("to")
m.push("be")
m.push("or")
m.push("not")
m.push("to")
m.push("-")
m.push("be")
m.push("--")
m.push("that")
m.push("---")
m.push("is")

print(m.size())

for i in range(0,m.size() - 1):
    print(i)
    if m.arr[i] != '-':
        print(m.arr[i])
    else:
        m.pop()
    
