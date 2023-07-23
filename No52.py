class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        for i in range(0,len(columnTitle)):
            res+=((ord(columnTitle[i])-ord('A')+1)*(26**(len(columnTitle)-i-1)))
        return res
    
print(Solution().titleToNumber("ZY"))