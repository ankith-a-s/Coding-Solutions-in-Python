class MinStack:
    def __init__(self):
        self.stack = []
        self.minOfStk = 0
    # @param x, an integer
    def push(self, val):
        if not self.stack:
            self.minOfStk = val
        if not self.stack or val >= self.minOfStk:
            self.stack.append(val)
        else:
            self.stack.append((2*val) - self.minOfStk)
            self.minOfStk = val


    # @return nothing
    def pop(self):
        if not self.stack:
            return 
        top = self.stack[-1]
        if top < self.minOfStk:
            self.minOfStk = (2 * self.minOfStk) - top
        self.stack.pop()

    # @return an integer
    def top(self):
        if not self.stack:
            return -1
        top = self.stack[-1]
        if top < self.minOfStk:
            return self.minOfStk
        else:
            return top

    # @return an integer
    def getMin(self):
        if not self.stack:
            return -1
        return self.minOfStk
