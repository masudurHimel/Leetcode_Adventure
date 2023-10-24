from collections import defaultdict 
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict()
        def dfs(root , level):
            if not root:
                return 
            if level in d.keys():
                d[level] = max( d[level] , root.val )
            else:
                d[level] = root.val

            dfs(root.left , level+1)
            dfs(root.right , level+1)

        dfs(root , 0)
        return d.values()