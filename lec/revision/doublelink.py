from linked import Node

class DoubleLinked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def add(self,e):
        temp = Node(e)
        if self.is_empty():
            self.head = temp
            self.tail = None
            self.size += 1
            return True
        elif self.tail is None:
            temp.next=  self.head.next
            temp.prev = self.head
            self.head.next = temp
            self.tail = temp
            self.size += 1
            return True
        else:
            temp.next= self.head.next
            temp.prev = self.head
            self.head.next = temp
            self.size += 1
            return True
        

    def print_list(self):
        this_node = self.head
        while this_node is not None:
            print(f"{this_node.data}", end="--")
            this_node = this_node.next
        print()

        return True
    
            
c = DoubleLinked()
c.add(5)
c.add(6)
c.add(8)
c.add(14)
c.print_list()
