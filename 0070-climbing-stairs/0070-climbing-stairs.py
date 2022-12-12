func climbStairs(n int) int {
    res := []int{0,1,2}
    if n <= 2{
        return res[n]
    }
    i:=3
    for ;i<=n;i++{
        res = append(res, res[i-1]+res[i-2])
    }
    return res[i-1]
}