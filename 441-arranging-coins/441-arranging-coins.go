func arrangeCoins(n int) int {
    res := 0
    l_i := n
    for i:=1;i<=l_i;i++{
        if i <= n{
            res++
            n -= i
        }else{
            break
        }
    }
    return res
}