class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees = sorted(trees)                                    
        upper, lower = [], []
        
        def interaction(X, Y, Z):                                      
            B1, B2, A1, A2, T1, T2 = chain(X, Y, Z)             
            return (T2-B2)*(B1-A1) - (B2-A2)*(T1-B1)
                   
        for i in trees:                                          
            while len(upper) >= 2 and interaction(upper[-1],upper[-2],i) < 0:      
                upper.pop()                                          
            upper.append(i)                                          
                                                                 
            while len(lower) >= 2 and interaction(lower[-1],lower[-2],i) > 0:      
                lower.pop()                                          
            lower.append(i)                                          
        return set(tuple(k) for k in (upper+lower))                      