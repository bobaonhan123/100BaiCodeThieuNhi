from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(mat)*len(mat[0]):
            return mat
        res=[]
        rnow=0
        cnow=0
        for i in mat:
            for j in i:
                if cnow==c:
                    rnow+=1
                    cnow=0
                if cnow==0:
                    res.append([])
                res[rnow].append(j)
                cnow+=1
        return res
print(Solution().matrixReshape([[1,2],[3,4]],1,4))