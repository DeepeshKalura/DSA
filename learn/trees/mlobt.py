from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.val = value
        self.left = left
        self.right = right

child11 = TreeNode(7)
child12 = TreeNode(-8)
child1 = TreeNode(7, child11, child12)
child2 = TreeNode(0)



class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        queue = deque([root])
        _max = -1
        _count = -1
        level = 0
        while queue:
            sum = 0
            level_size = len(queue)
            level+=1
            for _ in range(level_size):
                node = queue.popleft()
                sum+= node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            
            if(_max < sum):
                _max = sum 
                _count = level

        return _count
        

    

root = TreeNode(1, child1, child2)            
print(Solution().maxLevelSum(root))