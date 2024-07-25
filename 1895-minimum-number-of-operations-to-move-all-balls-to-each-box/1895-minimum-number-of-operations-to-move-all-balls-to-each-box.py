class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        solution = []
        int_box = []
        for x in boxes:
            int_box.append(int(x))
        i = 0
        while i < len(int_box):
            j = 0
            total = 0
            while j < len(int_box):
                diff = abs(i - j)
                total += (diff * int_box[j])
                j += 1
            solution.append(total)
            i += 1

        return solution