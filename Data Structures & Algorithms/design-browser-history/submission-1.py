class Page:
    def __init__(self, prev=None, url=None, next=None):
        self.prev = prev
        self.url = url
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Page(url=homepage)
        

    def visit(self, url: str) -> None:
        page = Page(url=url)
        self.curr.next = page
        page.prev = self.curr
        self.curr = page

    def back(self, steps: int) -> str:
        ptr = self.curr
        while ptr.prev and steps > 0:
            steps -= 1
            ptr = ptr.prev  

        self.curr = ptr
        return ptr.url

    def forward(self, steps: int) -> str:
        ptr = self.curr
        while ptr.next and steps > 0:
            steps -= 1
            ptr = ptr.next                    
        self.curr = ptr
        return ptr.url    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)