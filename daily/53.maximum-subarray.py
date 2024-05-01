#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _ms = -(10**4+1)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                _sum = sum(nums[i:j+1])
                if _sum > _ms:
                    _ms = _sum
        
        return _ms
        
# @lc code=end
nums = [-2,-1]
sol = Solution()
print(sol.maxSubArray(nums))
