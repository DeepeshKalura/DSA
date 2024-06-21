#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List

# TODO: Solve this question in the future
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        def recursion(index:int, path:List[int]):
            if(len(path) == len(nums)):
                result.append(path.copy())
                return 
            
            for i in range(len(nums)):
                path.append(nums[i])
                recursion(index+1, )

# @lc code=end

