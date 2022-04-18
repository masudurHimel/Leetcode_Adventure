class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for i in emails:
            strs = i.split('@')
            i = strs[0]
            i = ''.join(filter(lambda x: x != '.', i))
            try:
                p_ind = i.index('+')
                i = i[:p_ind]
            except Exception as e:
                pass
            
            i = i+'@'+strs[1]
            res.add(i)
        return len(res)