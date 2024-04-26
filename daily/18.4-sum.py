#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
from typing import List
from collections import defaultdict

#  it work but the time complexity is really high 
#  reduce one loop and binary search type will N3 logn maybe that will work
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        hm = defaultdict(int)
        res:List[List[int]] = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    value = target - (nums[i] + nums[j] + nums[k]) 
                    a = k+1
                    b = len(nums) - 1
                    while(a<=b):
                        mid = ( a + b ) // 2
                        if(nums[mid] > value):
                            b = mid -1
                        elif(nums[mid] < value):
                            a = mid + 1

                        else:

                            if (hm.get((nums[i] , nums[j] , nums[k] , value)) == None):

                                res.append([nums[i], nums[j], nums[k], value])

                                hm[(nums[i] , nums[j] , nums[k] , value)] += 1  

                            break

        return res

        
# @lc code=end


nums = [2,2,2,2,2]
target = 8
sol  = Solution()
print(sol.fourSum(nums, target))