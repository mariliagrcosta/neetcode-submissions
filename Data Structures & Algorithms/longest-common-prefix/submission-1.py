class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reference = strs[0]
        for idx in range(len(reference)):
            char = reference[idx]
            for i in range(1, len(strs)):
                if idx >=len(strs[i]) or strs[i][idx] != char:
                    return reference[:idx]
        return reference            