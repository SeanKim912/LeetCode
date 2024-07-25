class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        i = 0
        length = len(bank)
        while i < length - 1:
            r1 = bank[i]
            if "1" in r1:    
                r2 = ""
                j = i + 1
                while j < length:
                    if "1" in bank[j]:
                        r2 = bank[j]
                        j = length
                    else:
                        j += 1
                
                total += (r1.count("1") * r2.count("1"))
            i += 1

        return total