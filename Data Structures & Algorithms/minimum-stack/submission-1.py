class MinStack:
    # 题意：设计一个最小栈，要求在常数时间内获得栈中的最小值
    # 思路：因为这题要实现栈的功能，还要O(1)时间获取最小值。因此不能用最小堆（不能获取栈的顶端元素）。因此不能在 getMin()的时候再去计算最小值，最好应该在 push 或者 pop 的时候就已经计算好了当前栈中的最小值
    # 1. 新元素入栈：
        # 当栈为空，入栈元组 (x, x)；
        # 当栈不空，入栈元组 (x, min(此前栈内最小值, x))
    # 2. 出栈：删除栈顶的元组。
    # 因此，栈顶元素保存的是(x, 当前栈内最小值)，能在pop的时候同时获得这两个元素
    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append((val, val))
        else:
            cur_min = min(val, self.min_stack[-1][1])
            self.min_stack.append((val, cur_min))

    def pop(self) -> None:
        self.min_stack.pop(-1)
        
    def top(self) -> int:
        return self.min_stack[-1][0]
        

    def getMin(self) -> int:
        return self.min_stack[-1][1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()