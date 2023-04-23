from revision import double


def cyclic(head):
    this_node = head
    prev = None
    

    while True:
        if this_node.next == this_node:
            return False
        elif this_node.next == prev:
            return False
        prev = this_node
        this_node = this_node.next
    return True
