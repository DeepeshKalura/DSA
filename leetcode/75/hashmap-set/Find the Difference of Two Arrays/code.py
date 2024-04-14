from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = {}

        for i in arr:
            value = hm.get(i)
            if(value == None):
                hm[i] = 1
            else:
                hm[i] += 1
    
        
        flag:bool = False

        values = []

        for value in hm.values():
            values.append(value)

        
        values.sort()

        
        for i in range(1, len(values)):
            if(values[i-1] == values[i]):
                return False
        
        return True

arr = [1,2]
s = Solution()
print(s.uniqueOccurrences(arr))


            
        