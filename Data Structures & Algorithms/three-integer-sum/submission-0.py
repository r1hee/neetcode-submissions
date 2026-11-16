class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums) :
            if n > 0 :
                break
            
            if i > 0 and n == nums[i-1]:
                continue 

            a = i + 1
            b = len(nums) - 1

            while a < b :
                s = nums[a] + nums[b] + n
                if s > 0:
                    b -= 1 
                elif s < 0 :
                    a += 1
                elif s == 0 :
                    res.append([n, nums[a], nums[b]])
                    a += 1
                    b -= 1
                    while nums[a] == nums[a - 1] and a < b :
                        a += 1
        return res

                
