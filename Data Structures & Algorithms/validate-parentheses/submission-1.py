class Solution:
    def isValid(self, s: str) -> bool:
        # 注意：检查循环中 and 循环后 栈是否为空
        stack = []
        hashmap = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in '([{': # 如果是左括号，就把右括号入栈
                stack.append(hashmap[c])
            else:
                if not stack:
                    return False
                top = stack.pop(-1)
                if top != c:
                    return False

        return False if stack else True # 最后还要检查栈中元素是否已经匹配完了