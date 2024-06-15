#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start

# TODO: Write a solution in the leetcode
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        cs:int = 0
        timer:int = duration + timeSeries[0]
        for i in range(1, len(timeSeries)):
            if(timer > timeSeries[i]):
                cs+=(timeSeries[i] - timeSeries[i-1])
                timer = duration + timeSeries[i]
            else:
                cs+=duration
                timer = duration + timeSeries[i]
        
        return cs+duration

        
# @lc code=end

nums = [1,2,3,4,5,6,7,8,9]
duration = 1000
print(Solution().findPoisonedDuration(nums, duration))
