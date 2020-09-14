# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        prelength = len(preorder)
        inlength = len(inorder)
        if prelength <=0 or inlength <= 0:
            return None
        in_dict = dict()
        for i in range(inlength):
            in_dict[inorder[i]] = i
        ans = self.getBuildTree(preorder,0,prelength-1,inorder,0,inlength-1,in_dict)
        return ans
        
    def getBuildTree(self,preorder,pre_start,pre_end,inorder,in_start,in_end,in_dict):
        if pre_start > pre_end:
            return None
        root = TreeNode(preorder[pre_start])
        if pre_start == pre_end:
            return root
        else:
            root_index = in_dict[root.val]
            left_nodes = root_index - pre_start
            right_nodes = in_end - root_index
            left_node = self.getBuildTree(preorder,pre_start+1,pre_start+left_nodes,inorder,in_start,root_index-1,in_dict)
            right_node = self.getBuildTree(preorder,pre_end-right_nodes+1,pre_end,inorder,root_index+1,in_end,in_dict)
            root.left = left_node
            root.right = right_node
            return root
