class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList(object):
    def __init__(self):
        self.last = None

    def insertBeginning(self, value):
        pass

    def insertEnd(self, value):
        pass

    def deleteEnd(self):
        return - 1

    def displayAll(self):
        pass


CLL = CircularLinkedList()
CLL.insertBeginning(1)
CLL.insertBeginning(2)
CLL.displayAll()
CLL.insertEnd(3)
CLL.displayAll()
