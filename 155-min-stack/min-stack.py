class MinStack:

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        minVal = float('inf')
        if not self.stack:
            return None
        for n in self.stack:
            if n < minVal:
                minVal = n
        return minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()