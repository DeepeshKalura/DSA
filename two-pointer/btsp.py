from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        c:int = 0
        # 3 3 4 5
        # 1 2 2 3
        i:int = 0 
        while ( i < (len(people)-1)):
            c+=1
            a = people[i]
            b = limit - a 


            while(b >= people[i+1]):
                i+=1
                b = b - people[i]

                if(i+1 == len(people)):
                    return c

            i+=1

        

        c+=1
        return c 
    
print(Solution().numRescueBoats(people=[1,2], limit=3)) # 3