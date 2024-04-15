from typing import Optional


class TreeNode:

    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        if(self.root == None):
            self.root = TreeNode()
            self.root.val = value
        
        else:
            self._insert_recursion(self.root, value)
    
    def _insert_recursion(self, node , value):
        if(node.val < value):
            if node.right == None:
                node.right = TreeNode()
                node.right.val = value
            else:
                self._insert_recursion(node.right, value)
        else:
            if node.left == None:
                node.left = TreeNode()
                node.left.val = value
            else:
                self._insert_recursion(node.left, value)
    
    def inorder_traversal(self, head):
        if(head == None):
            return 
        self.inorder_traversal(head.left)
        print(head.val, end=" ")
        self.inorder_traversal(head.right)
    
    def dfs(self, head):
        if(head == None):
            return
        print(head.val, end=" ")
        self.dfs(head.left)
        self.dfs(head.right)




    def memo(self, root: Optional[TreeNode], rv: int):
        if not root:
            return 0
        rv = rv * 10
        rv += root.val

        if(not root.left and not root.right):
            return rv
        
        op=self.memo(root.left, rv)
        tp=self.memo(root.right, rv)
        
        return op+tp
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        _sum:int = root.val
        rv = root.valz
        _sum += self.memo(root.left, rv)
        _sum += self.memo(root.right, rv)
        return _sum
    




    def insert_tree(self, root, values, index):
        if index < len(values):
            if values[index] is not None:
                root = TreeNode(values[index])
                root.left = self.insert_tree(root.left, values, 2 * index + 1)
                root.right = self.insert_tree(root.right, values, 2 * index + 2)
        return root


array = [4,9,0,5,1]
tree = BinaryTree()

tree.root = tree.insert_tree(tree.root, array, 0)
# tree.inorder_traversal(tree.root)
print(tree.sumNumbers(tree.root))


    


