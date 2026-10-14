class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))

        p = 1
        for n in range(len(nums)) :
            #print(output[n])
            output[n] = p
            p *= nums[n]

        s = 1
        for m in range(len(nums)-1, -1, -1) :
            output[m] *= s
            s *= nums[m]

        return output


        