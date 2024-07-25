class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        solution = []
        i = 0
        while i < len(boxes):
            j = 0
            total = 0
            while j < len(boxes):
                diff = abs(i - j)
                total += (diff * int(boxes[j]))
                j += 1
            solution.append(total)
            i += 1

        return solution