from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res: List[int]=[]
        for i in nums1:
            ck=False
            isIn=False
            for j in nums2:
                if j==i:
                    ck=True
                    continue
                if ck and j>i:
                    res.append(j)
                    isIn=True
                    break
            if not isIn:
                res.append(-1)
        return res
    
print(Solution().nextGreaterElement([4,1,2],[1,3,4,2]))