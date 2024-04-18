from typing import Optional


class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.val = value
        self.left = left
        self.right = right


child11 = TreeNode(3)
child12 = TreeNode(4)
child1 = TreeNode(1, child11, child12)
child21 = TreeNode(3)
child22 = TreeNode(4)
child2 = TreeNode(2, child21, child22)
root = TreeNode(0, child1, child2)

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        val = chr(97 + root.val)

        np = self.smallestFromLeaf(root.left) + val
        nt = self.smallestFromLeaf(root.right) + val
        
        if(np > nt):
            return nt
        return np

print(Solution().smallestFromLeaf(root))
        