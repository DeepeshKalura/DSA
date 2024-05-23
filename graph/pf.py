from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        iv = [False] * len(isConnected)
        def dfs(start):
            if(iv[start] == True):
                return 0
            count:int = 1
            iv[start] = True

            for index, value in enumerate(isConnected[start]):
                if(value == 1):
                    if(not iv[index]):
                        count+=dfs(index)
            
            return count

        
        return len(isConnected) - dfs(0)
    
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))

        
        
        