from typing import List
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res=0
        for i in employees:
            if i.id==id:
                res+=i.importance
                for j in i.subordinates:
                    res+=self.getImportance(employees,j)
                break
        return res
print(Solution().getImportance([Employee(1,5,[2,3]),Employee(2,3,[]),Employee(3,3,[])],1))