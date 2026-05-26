class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for current_str in strs:
            char_frequency = [0] * 26
            for char in current_str:
                char_frequency[ord(char) - ord("a")] += 1
            key = tuple(char_frequency)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(current_str)
        return list(anagrams.values())
