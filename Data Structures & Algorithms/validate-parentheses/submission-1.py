class Solution:
    def isValid(self, s: str) -> bool:
        # push 
        stack = []
        for x in s:
            # push is fine if opening bracket
            # ( [ {
            if x == '(' or x == '[' or x == '{':
                stack.append(x)
            # check if top element is the same if closing bracket
            # pop if match
            elif x == ')' or x == ']' or x == '}':
                if len(stack) == 0:
                    return False
                if (stack[-1] == '(' and x == ')') or (stack[-1] == '[' and x == ']') or (stack[-1] == '{' and x == '}'):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
