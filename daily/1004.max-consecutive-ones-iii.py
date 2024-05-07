#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, zeros = 0, 0
        for r, n in enumerate(nums):
            zeros += n == 0
            if zeros > k:
                zeros -= nums[l] == 0
                l += 1
        return r - l + 1





# @lc code=end

sol = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(sol.longestOnes(nums, k))