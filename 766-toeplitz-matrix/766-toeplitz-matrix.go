func intSlicesEqual(a, b []int) bool {
    if len(a) != len(b) {
        return false
    }
    for i, v := range a {
        if v != b[i] {
            return false
        }
    }
    return true
}

func isToeplitzMatrix(matrix [][]int) bool {
    for i:=0;i<(len(matrix)-1);i++{
        if intSlicesEqual(matrix[i][:len(matrix[i])-1], matrix[i+1][1:len(matrix[i])]) == false{
            return false
        }
    }
    return true
}


// , matrix[i+1][0:len(matrix)]