class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue

                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        candidates.sort()
        backtrack(0, target, [])
        return result
        