class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = [char for char in s]
        t_list = [char for char in t]

        s_dict = {}
        t_dict = {}

        i = 0
        while i < len(s_list):
            curr = s_list[i]
            if curr not in s_dict:
                s_dict[curr] = 1
            else:
                s_dict[curr] += 1

            i += 1

        j = 0
        while j < len(t_list):
            curr = t_list[j]
            if curr not in t_dict:
                t_dict[curr] = 1
            else:
                t_dict[curr] += 1

            j += 1

        for letter in t_dict:
            if letter not in s_dict:
                return letter
            elif t_dict[letter] != s_dict[letter]:
                return letter