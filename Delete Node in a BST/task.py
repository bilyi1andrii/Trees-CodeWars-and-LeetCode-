# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root, key: int):
        if root is None:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.left is None:
                temp = root.right
                root = temp
            elif root.right is None:
                temp = root.left
                root = temp
            else:
                min_value = self.findMin(root.right)
                root.val = min_value
                root.right = self.deleteNode(root.right, min_value)
        return root

    def findMin(self, root):
        if root.left is None:
            return root.val
        return self.findMin(root.left)
