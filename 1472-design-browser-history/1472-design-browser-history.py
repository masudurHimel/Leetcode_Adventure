class BrowserHistory:

    def __init__(self, homepage: str):
        self.lst = [homepage]
        self.curr = 0
        

    def visit(self, url: str) -> None:
        self.lst = self.lst[:self.curr+1]
        self.lst.append(url)
        self.curr += 1
        

    def back(self, steps: int) -> str:
        # print(self.curr, self.lst[self.curr])
        self.curr = max(self.curr-steps, 0)
        # print(self.lst, self.curr, steps)
        return self.lst[self.curr]
        

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.lst)-1, self.curr + steps)
        return self.lst[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)