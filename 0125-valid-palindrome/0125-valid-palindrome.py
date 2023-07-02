class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        defStr = ""
        
        for c in s:
            if c.isalnum():
                defStr+=c.lower()
                
        return defStr == defStr[::-1]