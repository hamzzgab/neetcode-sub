class Logger:

    def __init__(self):
        self._hash = {}
        self.rate = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:        
        if (message in self._hash) and (timestamp < self._hash[message]):
            return False

        self._hash[message] = self.rate + timestamp
        return True

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
