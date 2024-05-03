#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1

        result = []
        for key, value in hm.items():
            if(value == 1):
                result.append(key)

        return result
        
# @lc code=end

