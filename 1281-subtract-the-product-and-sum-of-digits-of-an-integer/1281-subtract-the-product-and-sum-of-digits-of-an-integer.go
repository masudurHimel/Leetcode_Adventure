func subtractProductAndSum(n int) int{
    res_m := 1
    res_s := 0
    tmp := 0
    for n>0{
        tmp = n%10
        res_m *= tmp
        res_s += tmp
        
        n = n/10
    }
    
    
    return res_m - res_s
}