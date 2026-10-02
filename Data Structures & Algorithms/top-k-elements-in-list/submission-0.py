from collections import Counter
from collections import defaultdict

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items() :
            buckets[cnt].append(num)
        
        result = []
        for i in range(len(buckets)-1, 0, -1) :
            for n in buckets[i] :
               result.append(n)
               if len(result) == k :
                    return result

            
        

        