#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, zeroes  = 0, 0
        for i, value in enumerate(nums):
            zeroes += value == 0

            if zeroes > 1:
                zeroes -= nums[l] == 0
                l+=1

        return i - l
# @lc code=end
sol = Solution()
nums = [0,1,1,1,0,1,1,0,1]
print(sol.longestSubarray(nums))

