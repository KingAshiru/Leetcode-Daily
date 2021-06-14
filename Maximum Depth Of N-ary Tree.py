"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(root):
            if not root:
                return 0
            
            res = 0
            for child in root.children:
                res = max(dfs(child), res)
                
            return res+1
        
        return dfs(root)
