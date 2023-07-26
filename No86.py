from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp=[0 for i in range(len(cost))]
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return dp[-1]
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))