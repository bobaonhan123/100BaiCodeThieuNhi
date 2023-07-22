from typing import List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s12=s1+' '+s2
        arr=s12.split(" ")
        mp=dict()
        for i in arr:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        res=[]
        for i in mp:
            if mp[i]==1:
                res.append(i)
        return res

print(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour"))