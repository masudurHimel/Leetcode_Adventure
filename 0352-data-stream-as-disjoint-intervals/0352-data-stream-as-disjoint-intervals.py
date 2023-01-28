class SummaryRanges:

    def __init__(self):
        self.arr = [ ] 
        
    def addNum(self, value: int) -> None:
        if value not in self.arr : 
            self.arr.append(value)
            self.arr.sort( )

    def getIntervals(self) -> List[List[int]]:
        
        ans = [ ]
        start = -1
        cond = True
        if len(self.arr) == 1 : 
            return [[self.arr[0], self.arr[0]]]
        
        
        for i in range(len(self.arr) - 1 ) : 
            
            if cond : 
                start = self.arr[i]
            if self.arr[i + 1] - self.arr[i] == 1 : 
                cond = False 
            else : 
                cond = True 
                ans.append([start, self.arr[i]])
        
        if cond == False : 
            ans.append([start, self.arr[-1]])
        elif self.arr[-1] != self.arr[-2] : 
            ans.append([self.arr[-1], self.arr[-1]])
            
        return ans 