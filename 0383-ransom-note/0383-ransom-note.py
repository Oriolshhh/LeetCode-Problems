class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteMap = {}
        mgzMap = {}
        
        for char in ransomNote:
            noteMap[char] = noteMap.get(char, 0) + 1
    
        for char in magazine:
            mgzMap[char] = mgzMap.get(char, 0) + 1

        for key, value in noteMap.items():
            if key not in mgzMap or noteMap[key] > mgzMap[key]:
                return False
            mgzMap[key] -= noteMap[key]  
        
        return True