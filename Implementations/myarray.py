# A simple array based implementation of a Stack

# Stack class 
class ArrayStack:
    """
        data  -> keeps track of the data
        ###METHODS

        pop -> removal form the top
        push -> adds elements at the top 
        top -> returns element ontop of the stack
        is_empty -> return  true if stack is empty
        len -> returns the length of the stack
        
    """


    def __init__(self):
        self._data = []

    # returns the lenght of the stack
    def length(self):
        return len(self._data)


    # checks if the stack is empty
    def is_empty(self):
        return len(self._data)== 0
    
    # returns the topmost element
    def pop(self):
        return self._data.pop()

    #removes an element on the stack
    def top(self):
        if not self.is_empty():
            top = self._data[-1]
            return top 
        
    # adds an element to the stack
    def push(self,e):
        self._data.append(e)

    
    def __repr__(self):
        return f"stack : {self._data}"


if __name__ == '__main__':
    s = ArrayStack()
    s.push(5)
    s.push(3)
    print(s)
    print(s.top())
    s.pop()
    s.pop()
    print(s)
   

