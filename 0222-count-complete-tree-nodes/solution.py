# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        from collections import deque
        que=deque([root])
        count=0
        while que:
            node=que.popleft()
            count+=1
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return count
            


