class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reference = strs[0]
        common_prefix = ""
        for x in reference:
            common_prefix = common_prefix + x
            for i in range(1, len(strs)):
                if not strs[i].startswith(common_prefix):
                    return common_prefix[0: -1]
        return common_prefix            