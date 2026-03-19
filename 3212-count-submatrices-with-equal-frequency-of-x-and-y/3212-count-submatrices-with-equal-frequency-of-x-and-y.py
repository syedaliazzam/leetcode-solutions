class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        result = 0
        colsX = [0] * len(grid[0])
        colsY = [0] * len(grid[0])
        for y in range(len(grid)):
            curX = 0
            curY = 0
            for x in range(len(grid[y])):
                colsX[x] += 1 if grid[y][x] == 'X' else 0
                curX += colsX[x]
                colsY[x] += 1 if grid[y][x] == 'Y' else 0
                curY += colsY[x]
                if curX == curY and curX > 0:
                    result += 1
        return result