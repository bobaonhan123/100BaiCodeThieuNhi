from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    if i==0:
                        res+=1
                    if i==len(grid)-1:
                        res+=1
                    if j==0:
                        res+=1
                    if j==len(grid[0])-1:
                        res+=1
                    if i>0:
                        if grid[i-1][j]==0:
                            res+=1
                    if i<len(grid)-1:
                        if grid[i+1][j]==0:
                            res+=1
                    if j>0:
                        if grid[i][j-1]==0:
                            res+=1
                    if j<len(grid[0])-1:
                        if grid[i][j+1]==0:
                            res+=1
        return res
print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))