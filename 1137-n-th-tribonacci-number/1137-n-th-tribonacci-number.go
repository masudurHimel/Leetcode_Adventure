func tribonacci(n int) int {
    temp := [3]int{0,1,1}
    if n <= 2{
        return temp[n]
    }
    res := make([]int, n+1)
    res[0], res[1], res[2] = 0,1,1
    for i:=3;i<=n;i++{
        res[i] = res[i-1]+ res[i-2] + res[i-3]
    }
    return res[n]
}