class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.split(' ')
        res=''
        for i in arr:
            res+=' '
            for j in range(len(i)-1,-1,-1):
                res+=i[j]
        return res[1:]
    
print(Solution().reverseWords("Let's take LeetCode contest"))