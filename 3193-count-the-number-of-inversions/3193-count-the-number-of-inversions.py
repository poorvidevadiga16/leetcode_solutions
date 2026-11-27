class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7

        req = {end: cnt for end, cnt in requirements}

        max_inv = max(req.values()) if n - 1 in req else n * (n - 1) // 2

        dp = [0] * (max_inv + 1)
        dp[0] = 1

        for i in range(n):
            ndp = [0] * (max_inv + 1)
            window = 0

            for j in range(max_inv + 1):
                window += dp[j]

                if j - i - 1 >= 0:
                    window -= dp[j - i - 1]

                ndp[j] = window % MOD

            if i in req:
                cnt = req[i]
                for j in range(max_inv + 1):
                    if j != cnt:
                        ndp[j] = 0

            dp = ndp

        return sum(dp) % MOD

        