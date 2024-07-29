# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.children = 0
        def traverse(node):
            if not node:
                return 0
            if node.val % 2 == 0:
                if node.left and node.left.left:
                    self.children += node.left.left.val
                if node.left and node.left.right:
                    self.children += node.left.right.val
                if node.right and node.right.left:
                    self.children += node.right.left.val
                if node.right and node.right.right:
                    self.children += node.right.right.val

            return traverse(node.left) + traverse(node.right)
        
        traverse(root)
        return self.children