class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1

        while a < b :
            if target - numbers[a] == numbers[b] :
                return [a+1, b+1] 
            elif target - numbers[a] > numbers[b] :
                a += 1
            elif target - numbers[a] < numbers[b] :
                b -= 1
            
                