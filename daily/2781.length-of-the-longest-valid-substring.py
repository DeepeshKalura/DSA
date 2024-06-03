#
# @lc app=leetcode id=2781 lang=python3
#
# [2781] Length of the Longest Valid Substring
#

# @lc code=start
from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        i,k, n = 0, 1, len(word) 
        if(n==k):
            if(word in forbidden):
                return 0
            return k
        
        while(i+k < n):
            checker:bool = False
            for na in forbidden:
                w = word[i:k]
                if((na in w )):
                   checker = True 
            if(checker) :
                i+=1
                k+=1
            else:
                k+=1
            
        return k 
# @lc code=end
word = "bcac"
forbidden = ["bcac","caca","bcac","bca"]
print(Solution().longestValidSubstring(word, forbidden))
