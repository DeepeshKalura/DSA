#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        n = len(chars)
        i = 0
        while(n>0):
            value = chars.pop(0)
            n -= 1
            chars.append(value)
    
            count = 1
            while(n>0):
                next_val = chars[0]
                if(next_val != value):
                    break
                next_val = chars.pop(0)
                n -= 1
                count += 1
        
            
            if(count != 1):
                count = str(count)
                for i in count:
                    chars.append(i)

        return len(chars)

        


            

                




# @lc code=end


sol = Solution()
chars = ["a","a","a","b","b","a","a"]
sol.compress(chars)