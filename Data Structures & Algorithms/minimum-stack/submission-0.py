class MinStack:

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append((val, val))
        else:
            min_val = min(self.min_stack[-1][1], val)
            self.min_stack.append((val, min_val))

    def pop(self) -> None:
        self.min_stack.pop(-1)
        
    def top(self) -> int:
        return self.min_stack[-1][0]
        
    def getMin(self) -> int:
        return self.min_stack[-1][1]
        
