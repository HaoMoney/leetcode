#队列思想


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        out_list = []
        queue = []
        queue.append(root)
        while queue:
            res = []
            next_queue = []
            for one in queue:
                res.append(one.val)
                if one.left:
                    next_queue.append(one.left)
                if one.right:
                    next_queue.append(one.right)
            out_list.append(res)
            queue = next_queue
        return out_list
            
