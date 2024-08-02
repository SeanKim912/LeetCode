class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        i = len(garbage) - 1
        pile = "".join(garbage)
        total = len(pile)
        gmax = 0
        pmax = 0
        mmax = 0
        new_travel = [0] + travel
        while i >= 0:
            trash = garbage[i]
            if "G" in trash and not gmax:
                gmax = i + 1
                total += sum(new_travel[0:gmax])
            if "P" in trash and not pmax:
                pmax = i + 1
                total += sum(new_travel[0:pmax])
            if "M" in trash and not mmax:
                mmax = i + 1
                total += sum(new_travel[0:mmax])
            i -= 1

        return total