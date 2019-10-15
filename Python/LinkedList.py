class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.start = None

    def insertFront(self, value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
            return
        newNode.next = self.start
        self.start = newNode

    def insertRear(self, value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
            return
        ptr = self.start
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = newNode

    def deleteFront(self):
        if self.start == None:
            raise ValueError('Underflow')
        temp = self.start.value
        self.start = self.start.next
        return temp

    def deleteRear(self):
        if self.start == None:
            raise ValueError('Underflow')
        ptr1 = ptr2 = self.start
        while ptr1.next != None:
            ptr2 = ptr1
            ptr1 = ptr1.next
        ptr2.next = None
        return ptr1.value

    def displayAll(self):
        if self.start == None:
            raise ValueError('Underflow')
        ptr = self.start
        while ptr != None:
            print(ptr.value, end='->')
            ptr = ptr.next
        print()


# Test Code

L = LinkedList()
L.insertFront(1)
L.insertFront(2)
L.insertRear(3)
L.displayAll()
L.insertFront(4)
L.insertRear(5)
L.displayAll()
L.deleteFront()
L.deleteRear()
L.displayAll()
L.deleteRear()
L.displayAll()
