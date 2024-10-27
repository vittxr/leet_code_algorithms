opening_parentheses = ["(", "[", "{"]
map = {"{": "}", "[": "]", "(": ")"}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) == 1:
            return False

        for char in s:
            if char in opening_parentheses:
                stack.insert(0, char)
            else:
                if len(stack) > 0 and char == map.get(stack[0]):
                    stack.pop(0)
                else:
                    return False

        if len(stack) > 0:
            return False

        return True
