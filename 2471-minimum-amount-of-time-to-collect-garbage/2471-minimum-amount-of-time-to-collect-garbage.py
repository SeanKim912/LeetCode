class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        i = len(garbage) - 1
        pile = "".join(garbage)
        total = len(pile)
        gmax = 0
        pmax = 0
        mmax = 0
        while i >= 0:
            trash = garbage[i]
            if not gmax and "G" in trash:
                gmax = i + 1
            if not pmax and "P" in trash:
                pmax = i + 1
            if not mmax and "M" in trash:
                mmax = i + 1
            i -= 1
        new_travel = [0] + travel
        total += (sum(new_travel[0:gmax]) + sum(new_travel[0:pmax]) + sum(new_travel[0:mmax]))

        return total