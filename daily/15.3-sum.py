#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res:List[List[int]] = []
        hm = defaultdict(int)

        nums.sort()

        for i in range(len(nums)):
            j:int = 1+1
            k:int = len(nums) - 1
            while(j<k):
                value = (nums[i] + nums[j] + nums[k])
                if(value == 0):
                    tup = (nums[i], nums[j], nums[k])

                    if(hm.get(tup) == None):
                        hm[tup] += 1
                        res.append([nums[i], nums[j], nums[k]])
                    break
                elif(value > 0):
                    k-=1
                else:
                    k+=1
    
        return res



# @lc code=end

