# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList
class Solution:
    max_flag = None
    min_flag = None
    
    def dfs(self, node, coord):
            if not node:
                return
            self.tt[f'{coord[0]}|{coord[1]}'].add(node.val)
            
            
            self.max_flag = max(self.max_flag, coord[1])
            self.min_flag = min(self.min_flag, coord[1])
            
            self.dfs(node.left, (coord[0]+1, coord[1]-1))
            self.dfs(node.right, (coord[0]+1, coord[1]+1))
            
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.tt = defaultdict(SortedList)
        self.max_flag = -math.inf
        self.min_flag = math.inf
        ans = defaultdict(list)
        res = []

        self.dfs(root, (0,0))
        # print(self.tt)
        self.tt = dict(sorted(self.tt.items(), key=lambda k: int(k[0].split('|')[0])))
        # print(self.tt)
        
        for i, v in self.tt.items():
            key = i.split('|')[-1]
            ans[int(key)] += list(v)
            
        for i in range(self.min_flag, self.max_flag+1):
            if val := ans.get(i):
                    res.append(val)
        return res
