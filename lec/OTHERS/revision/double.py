class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Double:
    
    def __init__(self,head=None):
        self.head = head
        self.size = 0
        
    def add(self,e):
        if self.size == 0:
            self.head = Node(e)
            self.head.next = self.head
        else:
            new_node = Node(e,self.head.next)
            self.head.next = new_node
        self.size += 1
    
    def find(self,e):
        this_node = self.head
        while True:
            if this_node.data == e:
                return this_node
            elif this_node.next == self.head:
                return False
            this_node = this_node.next
    
    def remove(self,e):
        this_node = self.head
        prev = None 

        while True:
            if this_node.data == e:
                if prev is not None:
                    prev.next = this_node.next
                else:
                    while this_node.next != self.head:
                        this_node = this_node.next
                    this_node.next =  self.head.next
                    self.head = self.head.next
                self.size -= 1
                return False
            elif this_node.next == self.head:
                return False
            prev = this_node
            this_node = this_node.next

    def print_list(self):
        if self.head is  None:
            return 
        this_node = self.head
        print(this_node.data, end=' ')
        while this_node.next != self.head:
            this_node = this_node.next
            print(this_node.data, end=' ')
        print()

        


if __name__ == '__main__':
    d = Double()
    d.add(5)
    d.add(7)
    d.add(6)
    d.add(4)
    d.add(8)
    d.remove(7)
    d.remove(8)
    d.remove(4)
    d.remove(6)
    d.remove(5)
    d.print_list()
    