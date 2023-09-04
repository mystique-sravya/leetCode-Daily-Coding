class MinStack:

    def __init__(self):
        self.st = []
        self.mst = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.mst == []:
            self.mst.append(val)
        else:
            if self.st[-1] > self.mst[-1]:
                self.mst.append(self.mst[-1])
            else:
                self.mst.append(self.st[-1])

    def pop(self) -> None:
        self.st.pop()
        self.mst.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mst[-1]
        
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()