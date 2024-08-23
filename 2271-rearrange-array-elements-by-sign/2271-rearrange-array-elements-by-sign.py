class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for x in nums:
            if x > 0:
                pos.append(x)
            else:
                neg.append(x)

        result = []
        i = 0
        while i < len(pos):
            result.append(pos[i])
            result.append(neg[i])
            i += 1

        return result

