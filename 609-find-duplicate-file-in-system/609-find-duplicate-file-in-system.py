class Solution:
    def findDuplicate(self, paths):
        res = defaultdict(list)
        valid = False
        for i in paths:
            fd = i.split()
            fr = fd[0]
            for j in fd[1:]:
                k = j.split('(')
                res[k[-1][:-1]].append(fr+'/'+k[0])
        
        fres = []
        for i in res.values():
            if len(i) > 1:
                fres.append(i)
        return fres