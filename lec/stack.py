class  Stack():
    def __init__(self):
        self.stack = list()
    
    def push(self,e):
        self.stack.append(e)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    
    def str(self):
        return  f"{self.stack}"