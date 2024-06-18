#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start

# TODO: DO it Every DAY until you are able to understand similar logic

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        def recursion(start:int, path):
            if(start == len(digits)):
                result.append(path)
                return 
            
            sequence = keyboard[digits[start]]

            for i in sequence:
                recursion(start+1, path+i)

        
        recursion(0, "")

        return result
                




    
        
# @lc code=end


print(Solution().letterCombinations("23"))
