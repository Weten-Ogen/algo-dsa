
class Node:
    def __init__(self,data=None,next=None,prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class SingleList:
    def __init__(self) -> None:
         self.head = None
         self.size = 0
         self.tail = None

    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def add_list(self,e):
        for i in e:
            temp = Node(i, self.head)
            temp.next = self.head
            self.head = temp 
            self.size += 1

    
    def add(self,e):
        temp = Node(e,self.head)
        temp.next= self.head
        self.head = temp
        self.size += 1
        return True
    
    def find(self,e):
        this_node = self.head
        while this_node is not None:
            if this_node.data == e:
                return True
            else:
                this_node = this_node.next
        return False
    
    def remove(self,e):
        this_node = self.head
        prev = None
        while this_node is not None:
            if this_node.data != e:
                prev = this_node
                this_node = this_node.next
            else:
                prev.next = this_node.next
                self.size -= 1 
                return True
        return False
    
    def print_list(self):
        this_node = self.head
        while this_node is not None:
            print(f"{this_node.data} --", end=' ') 
            this_node = this_node.next
        print()
        return True

    def reverse_list(self):
        this_node = self.head
        prev = None
        while this_node is not None:
            temp = this_node
            if prev is not None:
                this_node.next = prev
            else:
                this_node.next = None
            prev = temp
            this_node = temp.next

    

if __name__   == "__main__" :
    b = SingleList()
    b.add_list([1,2,3,4,5])
    b.reverse_list()
    b.print_list()