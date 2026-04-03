class DynamicArray:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._top = 0
        self._arr = [None] * self._capacity

    def get(self, i: int) -> int:
        return self._arr[i]

    def set(self, i: int, n: int) -> None:
        self._arr[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self._arr[self._top] = n
        self._top += 1

    def popback(self) -> int:
        top_element = self._arr[self._top - 1]
        self._arr[self._top - 1] = None
        self._top -= 1
        return top_element

    def resize(self) -> None:
        self._capacity *= 2
        temp_arr = [None] * self._capacity
        for i in range(self._capacity // 2):
            temp_arr[i] = self._arr[i]
        self._arr = temp_arr

    def getSize(self) -> int:
        return self._top

    def getCapacity(self) -> int:
        return self._capacity