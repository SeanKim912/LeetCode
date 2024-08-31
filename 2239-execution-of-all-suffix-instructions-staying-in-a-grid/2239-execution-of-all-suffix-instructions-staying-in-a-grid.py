class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        def moves(path: str) -> int:
            counter: int = 0
            curry: int = startPos[0]
            currx: int = startPos[1]
            i: int = 0
            while i < len(path):
                move: str = path[i]
                if move == "R" and currx + 1 < n:
                    currx += 1
                    counter += 1
                    i += 1
                elif move == "L" and currx - 1 >= 0:
                    currx -= 1
                    counter += 1
                    i += 1
                elif move == "U" and curry - 1 >= 0:
                    curry -= 1
                    counter += 1
                    i += 1
                elif move == "D" and curry + 1 < n:
                    curry += 1
                    counter += 1
                    i += 1
                else:
                    return counter

            return counter

        result: List[int] = []
        while len(s) > 0:
            result.append(moves(s))
            s = s[1:]
        
        return result