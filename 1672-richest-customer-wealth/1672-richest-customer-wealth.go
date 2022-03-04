func maximumWealth(accounts [][]int) int {
    max_res := -9999999999
    res := 0
    for i:=0;i<len(accounts);i++{
        res = 0
        for j:=0;j<len(accounts[i]);j++{
            res += accounts[i][j]
        }
        if res > max_res{
            max_res = res
        }
    }
    return max_res
}