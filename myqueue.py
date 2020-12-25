class Element:
    def __init__(self, value=None):
        self.value = value
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

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
            return None
        takenelement = self.head
        self.head = takenelement.prev
        return takenelement.value

    def is_empty(self):
        if self.size is 0:
            return True
        return False

    def size_of_queue(self):
        return self.size

    def head_of_queue(self):
        return self.head.value

    def tail_of_queue(self):
        return self.tail.value

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
