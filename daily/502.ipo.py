#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
from typing import List

# TODO: Not be ale to solve
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        items = list(zip(profits, capital))    
        sorted_items = sorted(items, key=lambda x: x[1])
        
        
        total_profit:int = 0
        i:int  = 0
        while(k > i and  i<len(profits)):
            _m = []
            for values, key in sorted_items:
                if(key > w):
                    break 
                _m.append((key, values))
            
            if(_m == []):
                return total_profit
            
            _zx = max(_m , key=lambda x:x[1])

            sorted_items[_zx[0]] = (_zx[0], 0)
            

            total_profit += _zx[1]
            w += _zx[1] 

            i+=1

        
        return w

        
# @lc code=end

k = 1
w = 2
profits = [1,2,3]
capital = [1,1,2]

print(Solution().findMaximizedCapital(k,w,profits, capital))
