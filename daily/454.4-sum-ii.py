#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hm = defaultdict(int)
        count:int = 0
        n:int = len(nums1)
        for i in nums1:
            for j in nums2:
                hm[i+j] += 1
        
        for i in nums3:
            for j  in nums4:
                count += hm[-(i+j)]
            
        return count

# @lc code=end



sol = Solution()

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1, 2]
nums4 = [0, 2]

print(sol.fourSumCount(nums1, nums2, nums3, nums4))

