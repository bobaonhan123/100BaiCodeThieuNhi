class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = [0 for i in range(256)]
        check=0
        for i in s:
            mp[ord(i)]+=1
        res=0
        for i in mp:
            if not i%2:
                res+=i
            else:
                check=1
                res+=i-1
        if check:
            return res+1
        return res

    
print(Solution().longestPalindrome("abccccdd"))