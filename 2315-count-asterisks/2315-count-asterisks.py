class Solution:
    def countAsterisks(self, s: str) -> int:

        count = 0
        pair = 0

        for i in s:
            if i == '|':
                pair += 1

            elif i == '*' and pair % 2 == 0:
                count += 1

        return count
        