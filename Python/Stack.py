class node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None


class Stack(object):
    def __init__(self, value = None):
        self.top = node(value)
    
    def push(self, value):
        n1 = node(value)
        if self.top == None:
            self.top = n1
            return
        n1.next = self.top
        self.top = n1

    def pop(self):
        if self.top == None:
            raise ValueError('Underflow')
        temp = self.top.value
        self.top = self.top.next
        return temp

    def displayAll(self):
        if self.top == None:
            raise ValueError('Underflow')
        ptr = self.top
        while ptr != None:
            print(ptr.value, end=' ')
            ptr = ptr.next
        print()

# testing code

S = Stack(1)

S.push(2)
S.push(3)
S.displayAll()
S.push(4)
S.push(5)
S.displayAll()
S.pop()
S.pop()
S.displayAll()

