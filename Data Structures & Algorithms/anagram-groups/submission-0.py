class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = [[strs[0]]]
        for i in range(1, len(strs)):
            match_found = False
            for j in range(len(anagrams)):
                if sorted(strs[i]) == sorted(anagrams[j][0]):
                    anagrams[j].append(strs[i])
                    match_found = True
                    break
            if match_found == False:
                anagrams.append([strs[i]])
        return anagrams
        