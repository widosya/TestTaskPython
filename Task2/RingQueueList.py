class RingQueueList(object):
    def __init__(self, max_size = 10):
        # Initialize the RingQueue of a max_size if set, otherwise by default 10
        self.buffer = [None] * max_size
        self.head = 0
        self.tail = 0
        self.max_size = max_size

    def size(self):
        # Return size of RingQueue
        if self.tail >= self.head:
            return self.tail - self.head
        return self.max_size - self.head - self.tail

    def is_empty(self):
        # Return True if head of RingQueue equals to the tail, otherwise False
        return self.tail == self.head

    def is_full(self):
        # Return True if tail of RingQueue is one before the head, otherwise False
        return self.tail == (self.head-1) % self.max_size

    def dequeue(self):
        # Return an item at the front of the RingQueue and remove it
        if self.is_empty():
            raise IndexError("RingQueue is empty, unable to dequeue")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return item

    def enqueue(self, item):
        # Add an item at the back of the RingQueue, delete an item at the front if RingQueue is full
        if self.is_full():
            self.dequeue()
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size

    def get(self, index):
        # Return an item by index
        if self.is_empty():
            raise IndexError("RingQueue is empty, unable to get")
        return self.buffer[index]

    def front(self):
        # Return the item at the front of the RingQueue
        return self.buffer[self.head]

