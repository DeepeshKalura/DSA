#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        

        for asteroid in asteroids:

            while stack and asteroid < 0 < stack[-1]:

                if( abs(asteroid) > stack[-1]):
                    stack.pop()
                    continue
                elif ( abs(asteroid) == stack[-1] ):
                    stack.pop()
                
                break

            else:
                stack.append(asteroid)
            
                
        
        return stack


# @lc code=end

asteroids = [5,10, -5]
# [11 , 2]
print(Solution().asteroidCollision(asteroids))


