
class DynamicArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity

    def get(self, i):
        if not self.is_empty() and i < self.capacity:
            return self.array[i]
        return None

    def set(self, i, n):
        if i < self.capacity:
            self.array[i] = n

    def pushback(self, n):
        if self.is_full():
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self):
        if not self.is_empty():
            val = self.array[self.size-1]
            self.array[self.size-1] = None
            self.size -= 1
            return val
        return None

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == -1

    def resize(self):
        self.capacity *= 2
        self.array += [None] * (self.capacity // 2)

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity
