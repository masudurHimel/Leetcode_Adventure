class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        res = Counter(arr)
        m_res = max(res.values())
        
        for k,v in res.items():
            if v == m_res:
                return k
        
        return 0