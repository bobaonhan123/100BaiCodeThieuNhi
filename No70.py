from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        mp={
            1:"Gold Medal",
            2:"Silver Medal",
            3:"Bronze Medal"
        }
        sorted=[]
        sorted.extend(score)
        sorted.sort()
        sorted.reverse()
        res=[]
        for i in score:
            if sorted.index(i)+1 in mp:
                res.append(mp[sorted.index(i)+1])
            else:
                res.append(str(sorted.index(i)+1))
        return res
print(Solution().findRelativeRanks([5,4,3,2,1]))