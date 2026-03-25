class Solution:
    def canPartitionGrid(self, grid):

        m, n = len(grid), len(grid[0])

        total = 0
        rowSum = [0]*m
        colSum = [0]*n

        for i in range(m):
            for j in range(n):
                total += grid[i][j]
                rowSum[i] += grid[i][j]
                colSum[j] += grid[i][j]

        if total % 2 != 0:
            return False

        half = total // 2

        run = 0
        for i in range(m-1):
            run += rowSum[i]
            if run == half:
                return True

        run = 0
        for j in range(n-1):
            run += colSum[j]
            if run == half:
                return True

        return False