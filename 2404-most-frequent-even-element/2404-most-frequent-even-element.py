class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        numsMap = {}
        
        for num in nums:
            if num in numsMap: 
                numsMap[num] += 1
            elif num % 2 == 0:
                numsMap[num] = 1
        
        output = -1
        maxVal = -1
        for key, value in numsMap.items():
            if value > maxVal: 
                maxVal = value
                output = key
            if value == maxVal: 
                if key < output:
                    output = key
                    
        return output