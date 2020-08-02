# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        outlist = []
        def traverse(root: TreeNode):
            if root:
                outlist.append(root)
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        for i in range(1,len(outlist)):
            pre = outlist[i-1]
            after = outlist[i]
            pre.left = None
            pre.right = after
