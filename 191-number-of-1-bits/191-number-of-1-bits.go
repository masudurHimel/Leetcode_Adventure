func hammingWeight(num uint32) int {
    x := fmt.Sprintf("%b", num)
    res := 0
    
    for i:=0;i<len(x);i++{
        if x[i] == '1'{
            res++
        }
    }
    return res
}