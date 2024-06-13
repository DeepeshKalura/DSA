#
# @lc app=leetcode id=2037 lang=python3
#
# [2037] Minimum Number of Moves to Seat Everyone
#

# @lc code=start
from typing import List

# TODO: Implemented by three different methods
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        move:int = 0
        for i in range(len(seats)):
            move += abs(seats[i] - students[i])

        
        return move
# @lc code=end

#?  Note:
# 1. Just by sort
# 2. Using Priority Queue
# 3. Counting Sort

'''
Readme part

# Intuition
Just sort it 

# Approach
- sort both the list
- then subtract the change 
- add change to the move
- return the move

# Complexity
- Time complexity: $$O(nlogn)$$

- Space complexity: $$O(1)$$

# Code
```
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        move:int = 0
        for i in range(len(seats)):
            move += abs(seats[i] - students[i])

        
        return move
```

'''

