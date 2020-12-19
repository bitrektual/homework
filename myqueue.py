class Element:
    def __init__(self, value = None):
        self.value = value
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, newvalue):
        newelement = Element(newvalue)
        if self.head is None:
            self.head = newelement
            self.tail = self.head
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

    def size(self):
        lastinque = self.head
        sizeofqueue = 0
        while (lastinque):
            sizeofqueue = sizeofqueue + 1
            lastinque = lastinque.prev
        return sizeofqueue

    def clear(self):
        while (self.head):
            takenelement = self.head
            self.head = takenelement.prev
