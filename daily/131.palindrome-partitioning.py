#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List

# TODO: Can't do yet still look up solution and feel this greedy basdard
# TODO: Recurssion is damm hard
# TODO: Still We want to dance

class Solution:

    
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def recursion(index, value:List):
            if(len(s) == index):
                result.append(value)
                return 
            
            for end in range(index+1,len(s) + 1 ):
                print(f"{index}, {end}")
                print(s[index: end])
                if(s[index: end] == s[index: end][::-1]):
                    recursion(end, value+[s[index: end]])

        recursion(0, [])
        return result

        
# @lc code=end


s = "aab"
print(Solution().partition(s))