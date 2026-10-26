
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                a = s[left:right]
                b = s[left + 1:right + 1]
                return a == a[::-1] or b == b[::-1]

            left += 1
            right -= 1

        return True

        