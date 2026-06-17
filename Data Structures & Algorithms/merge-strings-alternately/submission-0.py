class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        len1, len2 = len(word1), len(word2)

        for i in range(max(len1, len2)):
            if i < len1:
                merged.append(word1[i])
            if i < len2:
                merged.append(word2[i])

        return "".join(merged)
