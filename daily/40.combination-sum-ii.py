#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []

        stack = []


        def backtrack(start:int, target:int):
            if(target == 0):
                result.append(stack[:])
                return 
            
            for i in range(start, len(candidates)):
                
                if(candidates[i] == candidates[i-1]):
                    continue
                
                if(candidates[i]<=target):
                    stack.append(candidates[i])
                    backtrack(i+1, target-candidates[i])
                    stack.pop()
                else:
                    break
                
                
    
        
        backtrack(0, target)
        return result


# @lc code=end
candidates = [10,1,2,7,6,1,5]
target = 8

print(Solution().combinationSum2(candidates, target))