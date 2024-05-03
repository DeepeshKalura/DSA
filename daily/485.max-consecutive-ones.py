#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, zeros = 0, 0
        for r, n in enumerate(nums):
            zeros += n == 0
            if zeros > 0:
                zeros -= nums[l] == 0
                l += 1
        return r - l + 1
                    

        
        
# @lc code=end

sol = Solution()
nums = [0,0,0,1, 1, 1, 0,0,1,1]

print(sol.findMaxConsecutiveOnes(nums))
