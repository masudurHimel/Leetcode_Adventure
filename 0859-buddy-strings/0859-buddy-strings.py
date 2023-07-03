class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        fs, fg = list(s), list(goal)
        if len(s) != len(goal):
            return False
        reg = []
        ab = []
        i = 0
        ind_l = []
        for f,s in zip(s, goal):
            if f == s:
                reg.append(f)
            else:
                ind_l.append(i)
                ab.append(f)
            i += 1

        if len(ab) == 2:
            fs[ind_l[0]] = ab[1]
            fs[ind_l[1]] = ab[0]
            return fs == fg
            
        if len(set(reg)) < len(reg) and len(ab) == 0:
            return True
        return False