#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        a = 1
        for i in range(len(nums)):        
            if(a==nums[i]):
                a+=1
        
        return a
# @lc code=end

