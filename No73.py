from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp=dict()
        res=[]
        mi=len(list1)+len(list2)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if i+j>mi:
                    break
                if list1[i]==list2[j]:
                    mi=i+j
                    if mi not in mp:
                        mp[mi]=[]
                    mp[mi].append(list1[i])
        return mp[mi]
print(Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))