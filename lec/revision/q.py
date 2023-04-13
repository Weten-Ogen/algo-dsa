from linked import SingleList


c= SingleList()
c.add_list([8,7,12,3455,54])


def reverse_q(head):
    current = head
    prev = None

    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev
    
c.print_list() 

def print_q(c):
    this_node = c

    while this_node is not None:
        print(f'{this_node.data}', end=' ')
        this_node = this_node.next
    print()

print_q(reverse_q(c.head))





