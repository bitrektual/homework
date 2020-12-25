class Element:
    def __init__(self, value=None):
        self.value = value
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = None

    def enqueue(self, newvalue):
        newelement = Element(newvalue)
        if self.head is None:
            self.head = newelement
            self.tail = self.head
            self.size = 1
            return
        lastelement = self.tail
        self.tail = newelement
        lastelement.prev = newelement
        self.size = self.size + 1

    def dequeue(self):
        if self.head is None:
            return 'Очередь пустая'
        takenelement = self.head
        self.head = takenelement.prev
        return takenelement.value

    def size(self):
        return self.size

    def head(self):
        return self.head

    def tail(self):
        return self.tail

    def clear(self):
        while (self.head):
            takenelement = self.head
            self.head = takenelement.prev
