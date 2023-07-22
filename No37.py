from typing import *
class Solution:
    def recursion(self,grid:List[List[int]],check:List[List[int]],posx,posy):
        if check[posy][posx]:
            return 0
        check[posy][posx]=1
        if not grid[posy][posx]:
            return 0
        res=1
        if posx>0:
            res+=self.recursion(grid,check,posx-1,posy)
        if posy>0:
            res+=self.recursion(grid,check,posx,posy-1)
        if posx<len(grid[0])-1:
            res+=self.recursion(grid,check,posx+1,posy)
        if posy<len(grid)-1:
            res+=self.recursion(grid,check,posx,posy+1)
        return res

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        check=[[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res=max(res,self.recursion(grid,check,j,i))
        return res
print(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))

        