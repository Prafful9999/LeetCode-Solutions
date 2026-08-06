# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        from collections import deque
        que=deque([root])
        hmap=set()
        while len(que)!=0:
            node=que.popleft()
            value=node.val
            if k-value in hmap:
                return True
            hmap.add(value)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return False
        
            