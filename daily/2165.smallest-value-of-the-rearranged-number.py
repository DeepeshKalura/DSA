#
# @lc app=leetcode id=2165 lang=python3
#
# [2165] Smallest Value of the Rearranged Number
#

# @lc code=start

from functools import cmp_to_key
from typing import List

class Solution:
    def smallestNumber(self, num: int) -> int:
        breaking:List[int] = []

        if(num>0):
            while (num!=0):
                i = num%10
                num = num//10
                breaking.append(i)

            
            breaking.sort()
            for i in range(len(breaking) -1):
# 50059
                if(breaking[i] == 0):
                    for j in range(i+1, len(breaking)):
                        if(breaking[j] != 0):
                            breaking[i], breaking[j] = breaking[j], breaking[i]
                            break
                    break
            num = "".join(map(str, breaking))

            return int(num)
        else:
            num = -num
            while (num!=0):
                i = num%10
                num = num//10
                breaking.append(i)
            breaking.sort(reverse=True)

            num = "".join(map(str, breaking))

            return -int(num)
        
# @lc code=end


num = 95005
sol = Solution()
print(sol.smallestNumber(num))

# nums = [2, 3, 6,1, 9, 0,  4]

# def sorting_logic(x, y):
#     if x + y > y + x:
#         return -1
#     elif x + y < y + x:
#         return 1
#     else:
#         return 0
    
# str_numbers = list(map(str, nums))
# print(str_numbers)
# tums = sorted(str_numbers, key=cmp_to_key(sorting_logic))

# print(tums)