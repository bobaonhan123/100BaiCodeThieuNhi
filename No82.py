from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        res=[]
        for i in nums1:
            l=0
            r=len(nums2)-1
            while l<=r:
                m=l+(r-l)//2
                if nums2[m]==i:
                    res.append(i)
                    nums2.remove(i)
                    break
                if nums2[m]>i:
                    r=m-1
                elif nums2[m]<i:
                    l=m+1
        return res
print(Solution().intersect([1,2,2,1], [2,2]))