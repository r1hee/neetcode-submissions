from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = defaultdict(int)
        for i in range(len(nums)) :
            d = target - nums[i]
            diffs[d] = i


        for n in range(len(nums)) :
            if nums[n] in diffs and diffs[nums[n]] != n:
                return [n, diffs[nums[n]]]
