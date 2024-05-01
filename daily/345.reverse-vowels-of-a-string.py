#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        i:int = 0
        j:int = len(s) - 1
        s = list(s)
        while(j>i):
            if(s[i] in vowels):
                if(s[j] in vowels):
                    s[i], s[j] = s[j], s[i]
                    i+=1
                    j-=1
                else:
                    j-=1

            else:
                i+=1
        
        return "".join(s)
        
# @lc code=end

