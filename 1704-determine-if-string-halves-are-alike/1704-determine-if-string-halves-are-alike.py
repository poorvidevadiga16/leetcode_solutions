
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        
        n = len(s) // 2
        
        a = sum(1 for ch in s[:n] if ch in vowels)
        b = sum(1 for ch in s[n:] if ch in vowels)
        
        return a == b

        