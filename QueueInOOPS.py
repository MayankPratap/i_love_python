class Queue(object):

    def __init__(self):
        """Create an empty queue"""
        self.vals=[] 

    def insert(self,e):
        self.vals.append(e)


    def remove(self):
        """ Removes front element of queue"""

        try:
            return self.vals.pop(0)
        except:
            raise ValueError("Queue is empty")


a=Queue()
a.insert(5)
a.insert(6)
print a.remove()

a.insert(7)
print a.remove()
print a.remove()

print a.remove() 
