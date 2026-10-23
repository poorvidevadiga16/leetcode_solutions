class Solution:
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        n = len(grid)
        
        if grid[0][0] != 0:
            return False

        pos = [None] * (n * n)

        for i in range(n):
            for j in range(n):
                pos[grid[i][j]] = (i, j)

        for k in range(1, n * n):
            r1, c1 = pos[k - 1]
            r2, c2 = pos[k]

            dr = abs(r1 - r2)
            dc = abs(c1 - c2)

            if not ((dr == 2 and dc == 1) or (dr == 1 and dc == 2)):
                return False

        return True
        