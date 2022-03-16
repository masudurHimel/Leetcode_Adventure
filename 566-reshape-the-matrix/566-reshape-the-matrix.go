func matrixReshape(mat [][]int, r int, c int) [][]int {
    if len(mat) * len(mat[0]) != r*c{
        return mat
    }
    target_list := make([]int, r*c)

    target_ind := 0
    
    for i:=0;i<len(mat);i++{
        for j:=0;j<len(mat[i]);j++{
            target_list[target_ind] = mat[i][j]
            // target_list = append(target_list, mat[i][j])
            // fmt.Print(target_list)
            target_ind++
        }
    }

    target_ind = 0
    // var res [r][c]int
    res := make([][]int, r)
    
    for i:=0;i<r;i++{
        for j:=0;j<c;j++{
            // res[i][j] = target_list[target_ind]
            res[i] = append(res[i], target_list[target_ind])
            target_ind++
        }
    }

    return res

}