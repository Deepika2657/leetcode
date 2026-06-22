# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def helper(root,leaves):
            if root is None:
                return False
            if root.left is None and root.right is None:
                leaves.append(root.val)
            helper(root.left,leaves)
            helper(root.right,leaves)
            return leaves
        return helper(root1,[])==helper(root2,[])
