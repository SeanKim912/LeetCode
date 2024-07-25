class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        i = 0
        length = len(bank)
        while i < length:
            string = bank[i]
            bank[i] = string.count("1")
            i += 1
        
        i = 0
        while i < length - 1:
            r1 = bank[i]
            r2 = 0
            j = i + 1
            while j < length:
                num = bank[j]
                if num:
                    r2 = num
                    j = length
                else:
                    j += 1
            total += (r1 * r2)
            i += 1

        return total