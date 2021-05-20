from array import ArrayType


class Queue:

    def __init__(self, maxSize):
        self.count = 0
        self.front = 0
        self.back = maxSize - 1
        self.qArray = ArrayType(maxSize)

    def isEmpty(self): 
        return self.count == 0
    
    def isFull(self):
        return self.count == len(self.qArray)

    def len(self):
        return self.count

    def enqueue(self, value):
        assert not self.isFull()
        maxSize = len(self.qArray)
        self.back = (self.back + 1) % maxSize
        self.qArray[self.back] = value
        self.count += 1
    
    def dequeue(self):
        assert not self.isEmpty()
        value = self.qArray[self.front]
        maxSize = len(self.qArray)
        self.count = (self.back + 1) % maxSize
        self.count -= 1
        return value
q = Queue

r = q.enqueue(8)
print(r)
