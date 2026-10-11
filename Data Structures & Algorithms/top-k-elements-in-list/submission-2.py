from collections import Counter
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = defaultdict(list)
        for i in range(len(nums)+1) :
            buckets[i] = []
        
        for key, cnt in count.items() :
            buckets[cnt].append(key)

        k_freq = []

        for n in range(len(buckets)-1, 0, -1) :
            for m in buckets[n] :
                k_freq.append(m)
                if len(k_freq) == k :
                    return k_freq
        
    
            
        

        