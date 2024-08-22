class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        col_max = len(grid[0])
        row_max = len(grid)
        diff = []
        row_count = []
        for x in grid:
            diff.append([])
            count = x.count(1)
            row_count.append(count - (row_max - count))

        col_count = []
        y = 0
        while y < col_max:
            count = 0
            for i in grid:
                if i[y] == 1:
                    count += 1
            col_count.append(count - (col_max - count))
            y += 1

        m = 0 
        while m < row_max:
            n = 0
            while n < col_max:
                diff[m].append(row_count[m] + col_count[n])
                n += 1
            m += 1

        return diff
