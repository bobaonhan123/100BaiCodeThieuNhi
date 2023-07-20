from typing import List
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            for j in range(len(image[i])//2):
                image[i][j],image[i][len(image[i])-1-j]=image[i][len(image[i])-1-j],image[i][j]
        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j]=int(not image[i][j])
        return image

print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))