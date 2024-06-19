#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start

# TODO: Not be able to solve
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        value = []
        hm = {}
        def recursion(start:int, swap:int):
            if(start == len(nums)):
                vt = "".join(str(value))
                if(not hm.get(vt)):
                    result.append(value.copy())
                    hm[vt] = 1

                return 
            
            
            
            while(swap > 0):
                value.append(nums[start])
                recursion(start+1, swap)

                nums[swap], nums[swap - 1] = nums[swap - 1], nums[swap]
                swap-=1
                value.clear()
                start = 0



        
        recursion(0, len(nums) - 1)

        return result
# @lc code=end


nums = [1,2,3]

print(Solution().permuteUnique(nums))