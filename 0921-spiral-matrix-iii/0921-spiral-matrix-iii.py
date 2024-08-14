class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        path = []
        total = rows * cols
        xmax = cols - 1
        ymax = rows - 1
        currx = cStart
        curry = rStart
        xinc = 1
        yinc = 1
        dist = 0
        compass = "east"

        while len(path) < total:
            validx = currx <= xmax and currx >= 0
            validy = curry <= ymax and curry >= 0
            if validx and validy:
                path.append([curry, currx])
            if compass == "east":
                currx += 1
                dist += 1
                if abs(dist) == xinc:
                    xinc += 1
                    dist = 0
                    compass = "south"
            elif compass == "south":
                curry += 1
                dist += 1
                if abs(dist) == yinc:
                    yinc += 1
                    dist = 0
                    compass = "west"
            elif compass == "west":
                currx -= 1
                dist -= 1
                if abs(dist) == xinc:
                    xinc += 1
                    dist = 0
                    compass = "north"
            elif compass == "north":
                curry -= 1
                dist -= 1
                if abs(dist) == yinc:
                    yinc += 1
                    dist = 0
                    compass = "east"

        return path