#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if(i == "*"):
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)
        
# @lc code=end

