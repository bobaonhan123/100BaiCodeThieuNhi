class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        resS=""
        resT=""
        for i in range(len(s)):
            if s[i]=='#':
                resS=resS[:-1]
            else:
                resS+=s[i]
        for i in range(len(t)):
            if t[i]=='#':
                resT=resT[:-1]
            else:
                resT+=t[i]
        return resS==resT
    
print(Solution().backspaceCompare("ab##","c#d#"))