from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i:int = 1
        j:int = 0
        stack = [asteroids[0]]
        while(i < len(asteroids) ):
            
            if(abs(stack[j] + asteroids[i]) > abs(asteroids[i])):
                stack.append(asteroids[i])
                j+=1
            else:
                
                while(len(stack) > 0):
                    value = stack.pop()
                    j-=1
                    
                    if(abs(value) > abs(asteroids[i])):
                        stack.append(value)
                        j+=1
                        break
                    elif (abs(value) == abs(value)):
                        break
                        
            i+=1
        
        return stack

sol = Solution()
asteroids = [-2,-1,1,2]
print(sol.asteroidCollision(asteroids))