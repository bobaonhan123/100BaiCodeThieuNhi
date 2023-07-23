from typing import List
class Solution:
    def recursion(self,grid:List[List[int]],posx,posy,color1,color2):
        if grid[posy][posx]!=color1:
            return grid
        grid[posy][posx]=color2
        if posx>0:
            grid=self.recursion(grid,posx-1,posy,color1,color2)
        if posy>0:
            grid=self.recursion(grid,posx,posy-1,color1,color2)
        if posx<len(grid[0])-1:
            grid=self.recursion(grid,posx+1,posy,color1,color2)
        if posy<len(grid)-1:
            grid=self.recursion(grid,posx,posy+1,color1,color2)
        return grid
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        self.recursion(image,sc,sr,image[sr][sc],color)
        return image
print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))