class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        piv = []
        prev = []
        after = []
        for x in nums:
            if x < pivot:
                prev.append(x)
            elif x > pivot:
                after.append(x)
            elif x == pivot:
                piv.append(x)
        
        return prev + piv + after