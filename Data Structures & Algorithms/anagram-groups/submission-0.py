from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha_dict = defaultdict(list)
        for i in range(len(strs)) :
            letters = [0] * 26
            for l in strs[i] :
                val = ord(l) - ord("a")
                letters[val] += 1
            alpha_dict[tuple(letters)].append(i)
        
        anagrams = []
        for key, value in alpha_dict.items() :
            anagrams.append([strs[i] for i in value])
        
        return anagrams
