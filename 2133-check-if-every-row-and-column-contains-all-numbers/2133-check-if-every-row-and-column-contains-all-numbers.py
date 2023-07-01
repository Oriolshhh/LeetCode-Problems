class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = collections.defaultdict(set) 
        columns = collections.defaultdict(set) 
        
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                num = matrix[r][c]
                if (num in rows[r] or num in columns[c]):
                    return False
                columns[c].add(num)
                rows[r].add(num)
        
        return True