class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ordered = sorted(piles)
        n = (len(piles)/3) * -2
        total = 0
        i = -2
        while i >= n:
            total += ordered[i]
            i -= 2

        return total