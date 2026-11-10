from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha_dict = defaultdict(list)

        for n in range(len(strs)) :
            letters = [0] * 26
            for l in strs[n] :
               val = ord(l) - ord("a")
               letters[val] += 1

            alpha_dict[tuple(letters)].append(n)
        
        anagrams = []

        for key, value in alpha_dict.items() :
            group = []
            for index in value :
                group.append(strs[index])
            
            anagrams.append(group)
        return anagrams