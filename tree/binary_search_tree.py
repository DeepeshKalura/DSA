from typing import Optional


class TreeNode:
    def __init__(self, val, left =None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right 

def inorder(root:Optional[TreeNode]):
    if not root:
        return 
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)
    return 

def find_min(root):
    while root.left:
        root = root.left
    return root


def delete_node(root:Optional[TreeNode], val:int): 
    if not root:
        return 
    

    if(root.val > val):
        root.right =  delete_node(root.right, val)
    
    elif (root.val < val):
        root.left = delete_node(root.left, val)

    else:
        if(not root.right):
            return root.left
        elif (not root.left):
            return root.right

        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)

    return root

def insert_node(value:int, root:Optional[TreeNode])-> Optional[TreeNode] :
    if( not root):
        root = TreeNode(value)
        return root

    if(root.val > value):
        root.right  = insert_node(value, root.right)
    else:
        root.left = insert_node(value, root.left)
    
    return root
        



array = [5,3,6,2,4,7]

root = None

for i in range(len(array)):
    root = insert_node(array[i], root)


inorder(root)
print()
