from typing import List
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res=[]
        for i in range(12):
            for j in range(60):
                if (i<<6|j).bit_count()==turnedOn:
                    res.append(str(i)+(":0" if j<10 else ":")+str(j))
        return res
print(Solution().readBinaryWatch(1))