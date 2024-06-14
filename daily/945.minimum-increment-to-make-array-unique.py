#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start
from typing import List

# TODO: I used solution please re-implemented that logic again and again
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        _max, _min = max(nums), min(nums)

        na = [0] * (_max - _min + len(nums))


        for i in nums:
            na[i - _min] += 1
        
        step, total = 0,0
        for i in na:
            step += i

            if(step > 0):
                step -= 1
            
            total += step

        
        return total
        
# @lc code=end

nums = [3,2,1,2,1,7]
print(Solution().minIncrementForUnique(nums))
