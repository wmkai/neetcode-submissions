class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == '+' or s == '-' or s == '*' or s == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                if s == '+':
                    stack.append(int(a + b))
                elif s == '-':
                    stack.append(int(a - b))
                elif s == '*':
                    stack.append(int(a * b))
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(s))
        return stack[0]
        