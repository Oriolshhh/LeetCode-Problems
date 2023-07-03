class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsMap = {}
        
        for num in nums:
            if num in numsMap:
                numsMap[num] += 1
            else:
                numsMap[num] = 1
                
        return max(numsMap, key=lambda k: numsMap[k])