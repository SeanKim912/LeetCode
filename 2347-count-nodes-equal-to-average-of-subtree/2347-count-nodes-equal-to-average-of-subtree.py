# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        counter = 0
        nodes = []

        def record(node):
            nodes.append(node)
            if node.left:
                record(node.left)
            if node.right:
                record(node.right)
        
        def traverse(node, values):
            values.append(node.val)
            if node.left:
                traverse(node.left, values)
            if node.right:
                traverse(node.right, values)
            
            return values

        record(root)
        for x in nodes:
            avg_list = traverse(x, [])
            print(avg_list)
            length = len(avg_list)
            if length > 0:
                if math.floor(sum(avg_list)/length) == x.val:
                    counter += 1

        return counter