class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1] == hashmap[c]:
                        stack.pop(-1)
                    else:
                        return False
            
        if not stack:
            return True
        else:
            return False