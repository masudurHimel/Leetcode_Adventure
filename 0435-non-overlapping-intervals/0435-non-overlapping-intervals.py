class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
			
        remove=0
        intervals=sorted(intervals, key=lambda x:x[1])
        
        startP=intervals[0][0]
        endP=intervals[0][1]
        
        for i in range(1,len(intervals)):
            startN=intervals[i][0]
            endN=intervals[i][1]
            
            if  startN<endP:
                remove+=1
            else:
                startP=startN
                endP=endN
                
        return remove  