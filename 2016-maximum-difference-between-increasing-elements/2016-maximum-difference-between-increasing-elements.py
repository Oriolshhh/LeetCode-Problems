class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i, j = 0, 1
        maxDif = -1 
        
        while j < len(nums):
            if nums[j] - nums[i] > maxDif and nums[j] - nums[i] != 0: 
                maxDif = nums[j] - nums[i]
            if nums[j] < nums[i]: 
                i = j
            
            j += 1
        
        return maxDif