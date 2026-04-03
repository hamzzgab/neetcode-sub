class Deque:

    def __init__(self):
        self._queue = []

    def isEmpty(self) -> bool:
        return len(self._queue) == 0

    def append(self, value: int) -> None:
        self._queue.append(value)

    def appendleft(self, value: int) -> None:
        self._queue = [value] + self._queue

    def pop(self) -> int:
        if not self.isEmpty():
            return self._queue.pop()
        return -1

    def popleft(self) -> int:
        if not self.isEmpty():
            return self._queue.pop(0)
        return -1
