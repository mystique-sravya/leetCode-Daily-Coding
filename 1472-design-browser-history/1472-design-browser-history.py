class Node:
    def __init__(self,url):
        self.prev = None
        self.next = None
        self.url = url
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
    def visit(self, url: str) -> None:
        self.head.next = Node(url)
        self.head.next.prev = self.head
        self.head = self.head.next

    def back(self, steps: int) -> str:
        while (self.head.prev != None and steps > 0):
            self.head = self.head.prev
            steps -= 1
        return self.head.url
        

    def forward(self, steps: int) -> str:
        while(self.head.next  !=None and steps > 0):
            steps -= 1
            self.head = self.head.next
        return self.head.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)