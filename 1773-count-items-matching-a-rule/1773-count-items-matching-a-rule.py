class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res_count = 0
        if ruleKey == 'type':
            target_ind = 0
        elif ruleKey == 'color':
            target_ind = 1
        else:
            target_ind = 2
            
        for i in items:
            if i[target_ind] == ruleValue:
                res_count += 1
        
        return res_count
            