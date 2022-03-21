class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for i in tokens:
            if i in '+-*/':
                b, a= res.pop(), res.pop()
                i = str(int(eval(a+i+b+'.')))
            res.append(i)
        
        return int(res[0])