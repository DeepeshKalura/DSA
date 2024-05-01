#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
from typing import List


class Solution:

    def countLenth(self, number:int)->int:
        number = str(number)
        return len(number)
    
    def largestNumber(self, nums: List[int]) -> str:

        def sorting_logic(nums):
            return str(nums) * 10          

        nums =  sorted(nums, key=sorting_logic, reverse=True)

        value = nums[0]

        for i in range(1, len(nums)):
            value *= 10**self.countLenth(nums[i])
            value += nums[i]

        return str(value)


        
# @lc code=end

sol = Solution()
nums = [3, 30, 34, 5, 9]
print(sol.largestNumber(nums))