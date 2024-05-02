#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = defaultdict(int)
        for value in s:
            hm[value] += 1 

        s:int = 0
        firstHit:bool = True
        for value in hm.values():
            if ( value % 2 == 0):
                s+=value 
            else:
                if(firstHit):
                    firstHit=False
                    s+=1
                
                else:
                    s+=value-1

    
        return s                    
# @lc code=end

s = "abccccdd"

print(Solution().longestPalindrome(s=s))