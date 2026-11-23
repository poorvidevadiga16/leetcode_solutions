
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        result = " ".join(words[:k])
        return result

        