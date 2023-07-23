from typing import List
from math import *
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area<=2:
            return [area,1]
        for i in range(ceil(area**0.5),1,-1):
            if area%i==0:
                tmp=[area//i,i]
                tmp.sort()
                return [tmp[1],tmp[0]]
        return [area,1]
print(Solution().constructRectangle(122122))