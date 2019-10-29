class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = self.prev = None


class DoublyLinkedList(object):
    def __init__(self):
        self.start = None

    def insertBeginning(self, value):
        newNode = Node(value)

        if self.start == None:
            self.start = newNode
            return

        self.start.prev = newNode
        newNode.next = self.start
        self.start = newNode

    def insertEnd(self, value):
        newNode = Node(value)

        if self.start == None:
            self.start = newNode
            return

        ptr = self.start
        while ptr.next != None:
            ptr = ptr.next
        newNode.prev = ptr
        ptr.next = newNode

    def deleteBeginning(self):
        if self.start == None:
            raise ValueError('Underflow')

        temp_node = self.start
        self.start = self.start.next
        self.start.prev = None
        return temp_node.value

    def deletEnd(self):
        if self.start == None:
            raise ValueError('Underflow')

        ptr = self.start
        while ptr.next != None:
            ptr = ptr.next
        temp_node = ptr
        ptr.prev.next = None
        return temp_node.value

    def displayAll(self):
        if self.start == None:
            raise ValueError('Underflow')

        ptr = self.start
        print('Forward Direction')
        while ptr is not None:
            last = ptr
            print(ptr.value, end='->')
            ptr = ptr.next
        print()

        print('Reverse Direction')
        while last is not None:
            print(last.value, end='->')
            last = last.prev
        print('\n')


# Test Code

DLL = DoublyLinkedList()

DLL.insertBeginning(1)
DLL.insertBeginning(2)
DLL.insertBeginning(3)
DLL.displayAll()
DLL.insertEnd(4)
DLL.insertEnd(5)
DLL.displayAll()
DLL.deleteBeginning()
DLL.deletEnd()
DLL.displayAll()
