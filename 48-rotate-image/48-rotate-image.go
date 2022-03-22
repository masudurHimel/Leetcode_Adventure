func rotate(matrix [][]int)  {
    for i:=0;i<len(matrix);i++{
        for j:=i+1;j<len(matrix);j++{
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        }
        
        for x, y := 0, len(matrix)-1; x < y; x, y = x+1, y-1 {
            matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]
        }
    }
}