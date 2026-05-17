class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1 
            else:
                s_dict[char] = 1       
        t_dict = {}
        for char in t:
            if char in t_dict:
                t_dict[char] += 1 
            else:
                t_dict[char] = 1
        if s_dict == t_dict:
            return True
        return False
        


        