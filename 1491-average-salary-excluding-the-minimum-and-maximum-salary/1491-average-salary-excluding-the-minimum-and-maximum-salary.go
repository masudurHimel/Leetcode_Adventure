func average(salary []int) float64 {
    max_sal := -999999999
    min_sal := 999999999
    total := 0
    
    for i:=0;i<len(salary);i++ {
        if salary[i] < min_sal{
            min_sal = salary[i]
        }
        
        if salary[i] > max_sal{
            max_sal = salary[i]
        }
        
        total += salary[i]
    }
    
    return float64(total - min_sal - max_sal) / float64(len(salary)-2)
    
}