#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
from typing import List



class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = second = third = float('inf')

        for num in nums:
            if(first>= num):
                first = num
            elif(second >= num):
                second = num
            elif (third >= num):
                return True
        
        return False
        
# @lc code=end

nums = [1,5,0,4,1,3]
sol = Solution()

print(sol.increasingTriplet(nums))
