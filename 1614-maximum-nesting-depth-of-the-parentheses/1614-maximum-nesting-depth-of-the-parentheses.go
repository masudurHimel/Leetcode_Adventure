func maxDepth(s string) int {
    
    count, max_count := 0,0
    for i:=0;i<len(s);i++{
        if s[i] == '('{
            count++
        }else if s[i] == ')'{
            count--
        }
        
        if count > max_count{
            max_count = count
        }
    }
    return max_count
}