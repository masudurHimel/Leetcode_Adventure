class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        
        x = {
            '2': 'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        res_dict = []
        for i in digits:
            res_dict.append(list(x[i]))
                            
        res = []
        
        for i in itertools.product(*res_dict):
            res.append(''.join(i))
        
        return res
        
        