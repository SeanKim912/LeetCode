class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ordered = sorted(piles)
        i = len(piles)/3
        total = 0
        while i > 0:
            skip = int(i * -2)
            total += ordered[skip]
            i -= 1

        return total