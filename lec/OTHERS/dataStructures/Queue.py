class Queue():
    def __init__(self):
        self.q = list()
    
    def enqueue(self,e):
         self.q.append(e)

    def dequeue(self):
        if len(self.q) > 0:
            ans = self.q[0];
        else: 
            return None
    
    
    