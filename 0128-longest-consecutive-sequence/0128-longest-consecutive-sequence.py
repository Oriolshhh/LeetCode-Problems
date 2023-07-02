class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxCount = 0
        
        for num in nums_set:
            if num - 1 not in nums_set:  #Start of a sequence 
                current_num = num
                counter = 1

                while current_num + 1 in nums_set: #While the sequence has next
                    current_num += 1
                    counter += 1

                maxCount = max(maxCount, counter) #Check the max

        return maxCount

    
        