func countNegatives(grid [][]int) int {
    count := 0
    for i:=0;i<len(grid);i++{
        fmt.Println(i)
        for j:=(len(grid[0])-1);j>=0;j--{
            fmt.Println(i,j)
            if grid[i][j] >= 0{
                break
            }else{
                count++
            }
        }
    }
    return count
}