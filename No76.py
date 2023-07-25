from typing import List
class Solution:
    def convert(self, img: List[List[int]],posy:int,posx:int) -> int:
        top=posy>0
        bottom=posy<len(img)-1
        left=posx>0
        right=posx<len(img[0])-1
        num=1
        num+=top+bottom+right+left+(top and left)+ (top and right)+(right and bottom)+(bottom and left)
        su=img[posy][posx]
        su+=(img[posy-1][posx] if top else 0) +(img[posy][posx-1] if left else 0)+(img[posy+1][posx] if bottom else 0)+(img[posy][posx+1] if right else 0)
        su+=(img[posy-1][posx-1] if top and left else 0)+(img[posy-1][posx+1] if top and right else 0)
        su+=(img[posy+1][posx-1] if bottom and left else 0)+(img[posy+1][posx+1] if bottom and right else 0)
        return su//num    
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res=[]
        for i in range(len(img)):
            res.append([])
            for j in range(len(img[0])):
                res[i].append(self.convert(img,i,j))
        return res
print(Solution().imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))
