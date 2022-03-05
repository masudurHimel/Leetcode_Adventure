func diagonalSum(mat [][]int) int {
    i, j := 0, len(mat) - 1
    res := 0
    for i < len(mat){
        res += mat[i][i]
        if i != j{
            res += mat[i][j]
        }
        i += 1
        j -= 1
    }
    return res
}