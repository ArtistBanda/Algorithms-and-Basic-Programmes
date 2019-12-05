class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList(object):
    def __init__(self):
        self.last = None

    def addToEmpty(self, value):
        newNode = Node(value)
        self.last = newNode
        self.last.next = newNode

    def insertBeginning(self, value):
        if self.last is None:
            self.addToEmpty(value)
            return
        newNode = Node(value)
        newNode.next = self.last.next
        self.last.next = newNode

    def insertEnd(self, value):
        if self.last is None:
            self.addToEmpty(value)
            return
        newNode = Node(value)
        newNode.next = self.last.next
        self.last.next = newNode
        self.last = newNode

    def deleteBeginning(self):
        if self.last is None:
            raise ValueError("Underflow")
        ptr = self.last.next
        self.last.next = ptr.next
        del ptr

    def displayAll(self):
        ptr = self.last.next
        while True:
            print(ptr.value, end=' ')
            ptr = ptr.next
            if ptr is self.last:
                print(ptr.value, end=' ')
                break
        print()

# Test Code


CLL = CircularLinkedList()
CLL.insertBeginning(1)
CLL.insertBeginning(2)
CLL.insertBeginning(3)
CLL.displayAll()
CLL.insertEnd(4)
CLL.displayAll()
CLL.deleteBeginning()
CLL.displayAll()
