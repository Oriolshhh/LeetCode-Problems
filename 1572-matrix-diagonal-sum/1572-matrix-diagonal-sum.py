class Solution:
        from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        output = 0
        matRange = len(mat) - 1

        while len(mat) > 0:
            if len(mat) == 1:
                output += mat[0][0]
            else:
                output += mat[0][0] + mat[0][matRange] + mat[matRange][0] + mat[matRange][matRange]

            if len(mat) > 1:
                mat = mat[1:matRange]
                for row in mat:
                    row.pop(0)
                    row.pop(matRange-1)
                matRange -= 2
            else:
                break

        return output
