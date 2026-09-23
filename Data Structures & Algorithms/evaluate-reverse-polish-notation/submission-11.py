class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == '+' or s == '-' or s == '*' or s == '/':
                # 注意：先弹出来的是第二个数
                b = int(stack.pop())
                a = int(stack.pop())
                if s == '+':
                    stack.append(int(a + b))
                elif s == '-':
                    stack.append(int(a - b))
                elif s == '*':
                    stack.append(int(a * b))
                else:
                    stack.append(int(a / b)) # 注意：除法要向0取整，不能用 //, //是向负无穷取整
            else:
                stack.append(int(s))
        return stack[0]
        