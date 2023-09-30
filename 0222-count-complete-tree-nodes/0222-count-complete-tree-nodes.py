# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

    # Calculate the height of the left and right subtrees
        left_height = 0
        left_node = root.left
        while left_node:
            left_height += 1
            left_node = left_node.left

        right_height = 0
        right_node = root.right
        while right_node:
            right_height += 1
            right_node = right_node.left

        # If left and right heights are equal, the left subtree is a full binary tree.
        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # If left and right heights are not equal, the right subtree is a full binary tree.
            return (1 << right_height) + self.countNodes(root.left)
