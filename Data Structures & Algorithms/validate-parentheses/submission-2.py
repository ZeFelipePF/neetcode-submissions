class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for letter in s:
            if letter in pairs:
                if not stack or stack[-1] != pairs[letter]:
                    return False
                stack.pop()
            else:
                stack.append(letter)

        return not stack