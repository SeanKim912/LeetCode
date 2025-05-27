class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = [char for char in s]
        t_list = [char for char in t]
        s_list.sort()
        t_list.sort()
        i = 0

        while i < len(t) - 1:
            if t_list[i] != s_list[i]:
                return t_list[i]
            else:
                i += 1
        
        return t_list[-1]