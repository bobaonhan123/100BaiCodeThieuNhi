from typing import List
from math import *
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        res=0
        for i in range(len(points)):
            mp=dict()
            for j in range(len(points)):
                if points[i]==points[j]:
                    continue
                if (points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2 not in mp:
                    mp[(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2]=0
                mp[(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2]+=1
            for k in mp.values():
                res+=k*(k-1)
        return res
print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))


