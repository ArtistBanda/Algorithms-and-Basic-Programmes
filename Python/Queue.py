class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None

class Queue(object):
    def __init__(self):
        self.front = self.rear = None

    def enQueue(self, value):
        newNode = Node(value)
        if self.front == None:
            self.front = self.rear = newNode
            return
        self.rear.next = newNode
        self.rear = newNode

    def deQueue(self):
        if self.front == None:
            raise ValueError('Underflow\n')
        nodeDel = self.front
        if self.front == self.rear:
            self.front = self.rear = None
            return nodeDel.value
        self.front = self.front.next
        return self.front.value

    def displayAll(self):
        if self.front == None:
            raise ValueError('Underflow\n')
        ptr = self.front
        while ptr != None:
            print(ptr.value, end=' ')
            ptr = ptr.next
        print()
    
# Test Code
Q = Queue()
Q.enQueue(1)
Q.enQueue(2)
Q.enQueue(3)
Q.enQueue(4)
Q.displayAll()
Q.deQueue()
Q.deQueue()
Q.displayAll()