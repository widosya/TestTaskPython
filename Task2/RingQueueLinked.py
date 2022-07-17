class Node(object):
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None

    def deletefirst(self):
        self.first = self.first.next

    def insert(self, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current


class RingQueueLinked(object):
    def __init__(self, max_size = 10):
        self.max_size = max_size
        self.cur_size = 0
        self.LinkedList = LinkedList()

    def size(self):
        # Return size of a RingQueue
        return self.cur_size

    def is_empty(self):
        # Return True if current size of RingQueue equals to zero, otherwise False
        return self.cur_size == 0

    def is_full(self):
        # Return True if current size of RingQueue equals to set max size, otherwise False
        return self.cur_size == self.max_size

    def dequeue(self):
        # Return Node at the front of RingQueue and remove it
        if self.is_empty():
            raise IndexError("RingQueue is empty, unable to dequeue")
        bufferitem = self.first
        self.LinkedList.deletefirst()
        self.cur_size -= 1
        return bufferitem

    def enqueue(self, item):
        # Add an item at the back of the RingQueue, delete an item at the front if RingQueue is full
        if self.cur_size == self.max_size:
            self.dequeue()
        self.LinkedList.insert(item)
        self.cur_size += 1

    def front(self):
        # Return first Node of the RingQueue
        return self.LinkedList.first()

    def back(self):
        # Return last Node of the RingQueue
        return self.LinkedList.last()





