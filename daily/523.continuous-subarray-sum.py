#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
# TODO: Medium Hard Question
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if(len(nums) < 2):
            return False


        
        sumArray = [nums[0]] 

        for i in range(1, len(nums)):
            sumArray.append(sumArray[i-1] + nums[i])
        i = 0
        j = len(nums) - 1

        while(i < j):
            if(nums[i] >= k):
                i+=1
            if(nums[j] >= k):
                j-=1

            if(sumArray[j] - sumArray[i] + nums[i] == k):
                result = 1
                for k in range(i, j+1):
                    result *= nums[k]

                if(result == k):
                    return True

        
        return False
        
# @lc code=end

nums = [23, 2, 4, 6,7]
k = 6

print(Solution().checkSubarraySum(nums, k))

