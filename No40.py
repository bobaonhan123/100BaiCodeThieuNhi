class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        check=[1 for i in range(len(s))]
        if len(s)==1:
            return 0
        res=0
        ma=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                check[i]=check[i-1]+1
            else:
                res+=min(ma,check[i-1])
                ma=check[i-1]
        return res-1+min(check[len(s)-1],ma)
print(Solution().countBinarySubstrings("10101"))