class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = []
        charMap = {')': '(', '}': '{', ']': '['}
        for char in A:
            if char in charMap:
                if not stack:
                    return 0
                top = stack.pop()
                if top != charMap[char]:
                    return 0
            else:
                stack.append(char)
        return 1 if len(stack) == 0 else 0
