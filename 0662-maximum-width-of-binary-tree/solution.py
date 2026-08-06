# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root):
        q = deque()
        q.append([root, 0])   # start from 0 better hai
        max_w = 0

        while len(q) != 0:
            n = len(q)
            
            first = q[0][1]   # first index
            last = q[-1][1]   # last index
            
            max_w = max(max_w, last - first + 1)

            for i in range(n):
                node, idx = q.popleft()
                
                if node.left:
                    q.append([node.left, 2*idx + 1])
                
                if node.right:
                    q.append([node.right, 2*idx + 2])
        
        return max_w