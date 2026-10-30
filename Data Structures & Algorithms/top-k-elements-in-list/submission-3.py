from collections import Counter
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frequent = defaultdict(list)
        for i in range(1, len(nums)+1) :
            frequent[i] = []
        
        for n, cnt in count.items() :
            frequent[cnt].append(n)
        
        k_most_frequent = []
        k_left = k
        for n in range(len(nums), 0, -1) :
            if k_left > 0 :
                k_most_frequent.extend(frequent[n])
                k_left -= len(frequent[n])
        
        return k_most_frequent

        
    
            
        

        