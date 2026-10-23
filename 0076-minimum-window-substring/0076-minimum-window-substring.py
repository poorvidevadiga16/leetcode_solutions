class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left = 0
        count = 0
        best = ""

        for right in range(len(s)):
            if s[right] in need:
                need[s[right]] -= 1
                if need[s[right]] >= 0:
                    count += 1

            while count == len(t):
                window = s[left:right + 1]

                if best == "" or len(window) < len(best):
                    best = window

                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        count -= 1

                left += 1

        return best
        