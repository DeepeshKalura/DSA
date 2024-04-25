#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = defaultdict(list)

        for i in range(len(nums)):
            hm[nums[i]].append((i, 1)) 


        for i in range(len(nums)):
            # one case will have issue
            value = hm.get(target-nums[i])

            if(value != None and i!= value[0][0]):
                return [i, value[0][0]]
        
        return [-1, -1]
            

# @lc code=end

sol = Solution()
nums = [3, 2, 4]
target = 6
print(sol.twoSum(nums, target))
