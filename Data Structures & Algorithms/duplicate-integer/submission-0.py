from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for n in nums :
            count[n] += 1

        for i in count.values() :
            if i > 1 :
                return True
        return False
