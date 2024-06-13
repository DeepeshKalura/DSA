#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
from typing import List
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        hm = {
            "(":")",
            "[":"]",
            "{": "}"
        }
        for i in s:
            if(i == '(' or  i == "[" or i == "{"):
                stack.append(i)
            
            elif(stack):
                if(hm[stack[-1]] == i):
                    stack.pop()
                else:
                    return  False
            else:
                return False
                

        

        return len(stack) == 0 
# @lc code=end

s = "(]"

print(Solution().isValid(s))