#
# @lc app=leetcode id=2511 lang=python3
#
# [2511] Maximum Enemy Forts That Can Be Captured
#

# @lc code=start
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        of:List[int] = []
        ef:List[int] = []
        for i in range(len(forts)):
            if(forts[i] == 1):
                of.append(i)
            elif(forts[i] == -1):
                ef.append(i)

        i = of[0]
        j = ef[-1]

        mc = 0
        count = 0
        while(i<j):
            if(forts[i] == 0):
                count+=1
            i+=1

        if(mc < count):
            mc = count
        
        i = of[-1]
        j = ef[0]

        while(i > j):
            if(forts[i] == 0):
                count+=1
            i-=1

        if(mc<count):
            mc = count
        

        return mc





# @lc code=end

