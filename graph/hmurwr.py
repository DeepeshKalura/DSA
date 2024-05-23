from collections import defaultdict
from typing import List


class Solution:
    

    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        iv = [False] * n # is visited ko manage kerna

        for i in restricted:
            iv[i] = True
        
        
        start:int = 0
        for i in range(len(iv)):
            if(iv[i]==False):
                start = i
                break
        
        def dfs(start:int):
            count:int = 1
            iv[start] = True
            for i in graph[start]:
                if (not iv[i]):
                    iv[i] = True
                    count+=dfs(i)
            
            return count

            

        return dfs(start)
        


        

n = 7
grid = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
restricted = [4, 5]
print(Solution().reachableNodes(n, grid, restricted))