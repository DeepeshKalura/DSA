from functools import reduce
from operator import xor
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        bo =  reduce(lambda a,b: a ^ b , nums)
        print(bo)
        return (bo^k).bit_count()
    
nums = [2,1,3,4]
k = 1
print(Solution().minOperations(nums, k))