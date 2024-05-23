# I fail to complete this question with my understanding of the graph
# let understand this question 



from queue import Queue
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        q = Queue()

        q.put((*entrance, 0))

        maze[entrance[0]][entrance[1]] = "+"

        ans=[]
        directions = [
            [0, 1], # j direction mey ek postive add kerna
            [1, 0], # i is direction badi matlab like ki tarf
            [0, -1] , # j is direction ko ganta hai or girana hai
            [-1, 0] # i value ko girai upper bane ke ley 
        ]
        while not q.empty():
            node = q.get()
            # print(node) 
            # end points ending check hogi
            if ((node[0] != entrance[0] or node[1] != entrace[1])):
                if(  ( (node[0] == 0 or node[0] == len(maze)-1) or (node[1] == 0  or node[1] == len(maze[0]) -1 )  )):
                    ans+=[node[2]]

            for i in range(len(directions)):
                x,y = node[0] + directions[i][0] , node[1] + directions[i][1]

                if( ( x>-1 and x<len(maze) ) and  ( y>-1 and y<len(maze[0]) )  ):
                    if(maze[x][y] == "."):
                        q.put((x, y, node[2]+1))
                        maze[x][y] = "+"

        print(ans)
        if(len(ans) == 0):
            return -1
        return min(ans)
            

maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrace = [1,0]
print(Solution().nearestExit(maze=maze, entrance=entrace))