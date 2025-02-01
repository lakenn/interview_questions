class BrowserHistory:

    def __init__(self, homepage: str):
        # [A, B, C, D]
        # .       curr = 2
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]

    # def visit(self, url: str) -> None:
    #     # clear up all the forward history
    #     self.stack = self.stack[:self.curr+1]
    #     self.stack.append(url)
    #     self.curr += 1

    # def back(self, steps: int) -> str:
    #     num = min(steps, self.curr)
    #     url = self.stack[self.curr - num]
    #     self.curr -= num
    #     return url

    # def forward(self, steps: int) -> str:
    #     num = min(steps, len(self.stack) - 1 -self.curr)
    #     url = self.stack[self.curr + num]
    #     self.curr += num
    #     return url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)