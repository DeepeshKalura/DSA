#
# @lc app=leetcode id=3147 lang=python3
#
# [3147] Taking Maximum Energy From the Mystic Dungeon
#

# @lc code=start
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ps = []
        for i in range(len(energy)):
            j = i+k
            eg = energy[i]
            while(j<len(energy)):
                eg+=energy[j]
                j+=k
            ps.append(eg) 
        print(ps)
        return max(ps)
# @lc code=end

