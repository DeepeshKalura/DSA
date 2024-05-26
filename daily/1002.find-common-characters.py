#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
# TODO: Didn't check the optimal solution please do
from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        main = words[0]
        result:List[str] = []
        cl:List[Counter] = []
        for i in range(1, len(words)):
            word = (Counter(words[i]))
            cl.append(word)
        

        n = len(words) - 1

        for x in main:
            counter:int = 0 
            for value in cl:
                if value[x] > 0:
                    counter+=1
                    value[x] -= 1
            if(counter == n):
                result.append(x)
            
            
        

        return result
                   
        
# @lc code=end


words = ["bella","label","roller"]

print(Solution().commonChars(words))

