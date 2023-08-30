class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.loc = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.loc] = item
            if self.loc == self.capacity - 1:
                self.loc = 0
            else:
                self.loc += 1

    def get(self):
        return self.storage
