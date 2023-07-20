class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res=0
        s1=set(jewels)
        for i in range(len(stones)):
            res+=stones[i] in s1
        return res

print(Solution().numJewelsInStones("aA","aAAbbbb"))
