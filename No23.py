from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res:List[List[int]]=[]
        for i in range(len(matrix[0])):
            res.append([])
            for j in range(len(matrix)):
                res[len(res)-1].append(matrix[j][i])
        return res
print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))