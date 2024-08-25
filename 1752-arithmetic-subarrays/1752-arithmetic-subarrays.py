class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        def check(x, y):
            if y - x <= 1:
                return True
            sub = sorted(nums[x : y + 1])
            diff = sub[1] - sub[0]
            i = 1
            length = len(sub) - 1
            while i < length:
                if sub[i] + diff != sub[i + 1]:
                    return False
                else:
                    i += 1
            return True

        i = 0
        length = len(l)
        while i < length:
            result.append(check(l[i], r[i]))
            i += 1

        return result