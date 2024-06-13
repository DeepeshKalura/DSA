#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from operator import add, sub, truediv, mul
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        hm = {"+" : add, "-" : sub, "*" : mul, "/": truediv}
        for i in tokens:
            if (i in hm.keys()):
                    number1 = int(stack.pop())
                    number2 = int(stack.pop())
                    res:int =  int(hm[i](number2,  number1))
                    stack.append(str(res))

            else:
                stack.append(i)

        
        return int(stack[-1])
    

# @lc code=end


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))