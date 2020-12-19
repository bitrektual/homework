class Element:
    def __init__(self, value):
        self.value = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, newvalue):
        newelement = Element(newvalue)
        if self.head is None:
            self.head = newelement
            return
        lastelement = self.tail
        self.tail = newelement
        lastelement.prev = newelement

    def dequeue(self):
        if self.head is None:
            return 'Очередь пустая'
        takenelement = self.head
        self.head = takenelement.prev
        return takenelement.value
