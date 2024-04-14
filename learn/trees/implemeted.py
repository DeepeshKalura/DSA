class TreeNode:

    def __init__(self):
        self.val = None
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



array = [5,6,3,1,4]
tree = BinaryTree()

for i in range(len(array)):
    tree.insert(array[i])


# tree.inorder_traversal(tree.root)
tree.dfs(tree.root)
print()


    


