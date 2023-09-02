class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        # Push the new element onto q1
        self.q1.append(x)
        
        # Move elements back from q2 to q1
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self):
        if self.q1:
            return self.q1.popleft()
    
    def top(self):
        if self.q1:
            return self.q1[0]
    
    def empty(self):
        return not bool(self.q1)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()