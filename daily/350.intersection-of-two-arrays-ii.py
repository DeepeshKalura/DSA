#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if(len(nums1) > len(nums2)) : return self.intersect(nums2, nums1)


        cnt  = Counter(nums1)
        result = []
        for x in nums2:
            if(cnt[x] > 0):
                result.append(x)

                cnt[x] -= 1 


        return result

# @lc code=end

nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersect(nums1, nums2))

