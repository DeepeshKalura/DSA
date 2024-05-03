#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        ps = 0
        res = 0
        hm[0] += 1
        for val in nums:
            ps+=val

            res+=hm[ps-k]
            
            hm[ps] += 1

        
        return res
        
# @lc code=end

nums = [0,0]
k = 0
sol = Solution()
print(sol.subarraySum(nums, k))