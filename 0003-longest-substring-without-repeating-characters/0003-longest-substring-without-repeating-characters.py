class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSeq = 0
        
        if len(s) == 0: return maxSeq
        
        for i in range(len(s)):
            lettersSet = set()
            counter = 0
            for j in range(i, len(s)):
                if s[j] not in lettersSet:
                    counter += 1
                    lettersSet.add(s[j])
                else:
                    break
            maxSeq = max(maxSeq, counter)
        
        return maxSeq