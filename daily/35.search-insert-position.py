#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        i = 0
        j = len(nums) - 1

        mid:int = 0 
        while(i <= j):
            mid = (i + j) // 2

            if(nums[mid] == target):
                return mid

            elif(nums[mid] > target):
                j = mid - 1 
            
            else:
                i = mid + 1

        return i
        
# @lc code=end

nums = [1,3,5,6]
target = 5

print(Solution().searchInsert(nums, target))