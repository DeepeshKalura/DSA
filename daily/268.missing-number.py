#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = n * (n + 1) // 2
        return _sum - sum(nums)
    
        
# @lc code=end

