class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = 99999999
        max_sal = -99999999
        total = 0
        
        for i in salary:
            if i < min_sal:
                min_sal = i
            if i > max_sal:
                max_sal = i
                
            total += i
        
        return (total-min_sal-max_sal)/(len(salary)-2)