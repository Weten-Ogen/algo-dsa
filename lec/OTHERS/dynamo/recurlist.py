class Node:
    def __init__(self,data):
        self.val = data
        self.next = None




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)



def recurList(head, ans=[]):

    if head == None:
        return ans
    ans.append(head.val)
    return recurList(head.next,ans)
    
#Suming a linked list 
# def summin(head, accumulator=0):
#     if head == None: return accumulator
#     accumulator = head.val + accumulator
#     return summin(head.next,accumulator)

# Insert Node Problems




a.next = b;
b.next = c;
c.next = d;
d.next = e;

def insect(head, value):
    if head == None:
        head = Node(value)
        return head
    
    if head != None:
        curr = Node(value)
        curr.next = head;
        head=curr
        return head
   
    return insect(head.next,value)


a = insect(a,70)
a = insect(a,669)
print(recurList(a))