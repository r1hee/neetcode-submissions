from collections import Counter
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = defaultdict(list)

        for n in range(len(nums)+1) :
            buckets[n] = []
        
        for key, cnt in count.items() :
            buckets[cnt].append(key)
        
       
        most_frequent = []
        for i in range(len(buckets)-1, 0, -1) :
            for n in buckets[i] :
                most_frequent.append(n)
                if len(most_frequent) == k :
                    return most_frequent

        
    
            
        

        