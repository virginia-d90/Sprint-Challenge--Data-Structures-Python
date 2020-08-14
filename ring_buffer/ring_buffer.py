class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index = 0


    def append(self, item):
        if len(self.data) < self.capacity:
           self.data.append(item)
        else:
            self.data[self.index] = item
            self.index = (self.index+1) % self.capacity

    def get(self):
        return self.data