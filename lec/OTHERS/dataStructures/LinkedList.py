# class Node: 
#     def __init__(self, d, n=None, p=None):
#         self.data = d
#         self.next_node = n
#         self.prev_node = p

#     def __str__(self):
#         return ('('+ str(self.data) + ')')
    

# # Single Linked List

# class LinkedList:

#     def __init__(self , r=None) -> None:
#         self.root = r
#         self.size = 0

#     # adding an element
#     def add(self, d):
#         new_node = Node(d, self.root)
#         self.root = new_node
#         self.size += 1

#     # finding an element
#     def find(self, d):
#         this_node = self.root
#         while this_node is not None:
#             if this_node.data == d:
#                 return d
#             else:
#                 this_node = this_node.next_node
#         return None
    
#     # removing an item
#     def remove(self, d):
#         this_node = self.root
#         prev_node = None

#         while this_node is not None:
#             if this_node.data  == d:    
#                 if prev_node is not None:
#                     prev_node.next_node = this_node.next_node
#                 else:
#                     self.root = this_node.next_node
#                 self.size -= 1
#                 return True
#             else:
#                 prev_node = this_node
#                 this_node = this_node.next_node
#         return False

    
#     def print_list(self):
#         this_node = self.root

#         while this_node is not None:
#             print(this_node, end='->')
#             this_node = this_node.next_node
#         print('None')


# # myList = LinkedList();
# # myList.add(5)
# # myList.add(8)
# # myList.add(12)
# # myList.print_list()
# # print(f"size {myList.size}")
# # myList.remove(8)
# # myList.print_list()
# # print(f"size {myList.size}")
# # print(myList.find(5))
# # print(myList.root)

class Node: 
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    

class SinList:
    def __init__(self,head=None):
        self.head = head
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def add(self,d):
        self.head = Node(d, self.head)
        self.size += 1
    
    def find(self, d):
        this_node = self.head
        while this_node is not None:
            if this_node.data == d:
                return True
            else:
                this_node = this_node.next
        return False
    
    def remove(self, d):
        this_node = self.head
        prev = None

        while this_node is not None:
            if this_node.data == d:
                if prev is not None:
                    prev.next = this_node.next
                else:
                    self.head = this_node.next
                self.size += 1
                return True
            else:
                prev = this_node
                this_node = self.head.next
        return False
                


    def get_size(self):
        return self.size
     
    def print_list(self):
        this_node = self.head

        while this_node is not None:
            print(this_node.data,end='--')
            this_node = this_node.next
        print('None')


l = SinList()
l.add(5)
l.add(6)
l.add(8)
l.print_list()
