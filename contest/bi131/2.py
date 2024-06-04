from collections import defaultdict
from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:

        hm = defaultdict(list)

        for i in range(len(nums)):
            hm[nums[i]].append(i)

        
        res = []


        for q in queries:
            value = hm.get(x)
            if(value == None):
                res.append(-1)
            
            elif(len(value) >= q ):
                res.append(value[q-1])
            else:
                res.append(-1)
        
        return res