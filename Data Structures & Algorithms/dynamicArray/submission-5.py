class DynamicArray:
    
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._length = 0
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None: 
        if self._length == self._capacity:
            self.resize()
        self.arr[self._length] = n
        self._length += 1

    def popback(self) -> int:
        if self._length > 0:
            self._length -= 1          
            temp = self.arr[self._length]
            self.arr[self._length] = None
            return temp  

    def resize(self) -> None:
        self._capacity *= 2
        new_arr = [None] * self._capacity

        # copy elements to new array
        for i in range(self._length):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def getSize(self) -> int:
        return self._length
    
    def getCapacity(self) -> int:
        return self._capacity