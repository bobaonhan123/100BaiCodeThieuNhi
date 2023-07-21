from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        ma=0
        r=len(arr)-1
        while l<=r:
            if arr[l]>=arr[l-1] and arr[l]>=arr[l+1]:
                return l
            if arr[r]>=arr[r-1] and arr[r]>=arr[r+1]:
                return r
            m=l+(r-l)//2
            if(arr[m]>ma):
                ma=arr[m]
                if arr[m]>=arr[m-1] and arr[m]>=arr[m+1]:
                    return m
            if arr[m-1]<arr[m]:
                l=m+1
            else:
                r=m-1
print(Solution().peakIndexInMountainArray([3,4,11,15,18,24,30,36,44,57,62,64,68,88,90,91,99,100,81,74,61,55,49,39,23,15,11]))