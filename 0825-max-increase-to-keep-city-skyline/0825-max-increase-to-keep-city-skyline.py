class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ymax = []
        length = len(grid)
        total = 0

        j = 0
        while j < length:
            highest = 0
            for k in grid:
                num = k[j]
                if num > highest:
                    highest = num
            ymax.append(highest)
            j += 1
        
        y = 0
        while y < length:
            for x in grid:
                xmax = max(x)
                vert = ymax[y]
                num = x[y]
                if num < xmax and num < vert:
                    total += (min(xmax, vert) - num)
            y += 1

        return total
                