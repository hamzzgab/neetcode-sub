class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:   
        if self.getCapacity() == self.getSize():
            self.resize()
        for i, val in enumerate(self.arr):
            if val == None:
                break
        self.arr[i] = n

    def popback(self) -> int:
        lastIndex = self.getSize() - 1
        temp = self.arr[lastIndex]
        self.arr[lastIndex] = None
        return temp

    def resize(self) -> None:
        n = len(self.arr)
        self.arr += [None] * n

    def getSize(self) -> int:
        count = 0
        for i in self.arr:
            if i != None:
                count += 1
        return count
    
    def getCapacity(self) -> int:
        return len(self.arr)