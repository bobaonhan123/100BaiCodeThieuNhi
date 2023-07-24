from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if s==[]:
            return 0
        g.sort()
        s.sort()
        res=0
        index=0
        for i in g:
            if(index==len(s)):
                break
            while i>s[index]:
                index+=1
                if index==len(s):
                    break
            if(index==len(s)):
                break
            res+=1
            index+=1

        return res
print(Solution().findContentChildren([1,2,3], [1,2]))