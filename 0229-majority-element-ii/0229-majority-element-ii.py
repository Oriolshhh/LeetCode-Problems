class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        minimum = len(nums) // 3
        numsMap = {}
        
        for num in nums:
            if num in numsMap: 
                numsMap[num] += 1
            else: 
                numsMap[num] = 1
                
        output = []        
        for key, value in numsMap.items(): 
            if value > minimum:
                output.append(key)
                
        return output