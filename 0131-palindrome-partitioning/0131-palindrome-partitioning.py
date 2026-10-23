class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []

        def isPalindrome(x):
            return x == x[::-1]

        def backtrack(start, current):
            if start == len(s):
                result.append(current[:])
                return

            for end in range(start + 1, len(s) + 1):
                part = s[start:end]

                if isPalindrome(part):
                    current.append(part)
                    backtrack(end, current)
                    current.pop()

        backtrack(0, [])
        return result
        