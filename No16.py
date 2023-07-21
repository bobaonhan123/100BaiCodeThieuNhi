from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in operations:
            if i=='+':
                res.append(res[-1]+res[-2])
            elif i=='D':
                res.append(res[-1]*2)
            elif i=='C':
                res=res[:-1]
            else:
                res.append(int(i))
        resNum=0
        for i in res:
            resNum+=i
        return resNum
    
print(Solution().calPoints(["5","2","C","D","+"]))