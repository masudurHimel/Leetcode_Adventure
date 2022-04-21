func searchMatrix(matrix [][]int, target int) bool {
    var l,r,mid int
    for i:=0;i<len(matrix);i++{
        if matrix[i][0] <= target{
            l,r = 0, len(matrix[i])-1
            for l<=r{
                mid = (l+r)/2
                if matrix[i][mid] == target{
                    return true
                }else if matrix[i][mid] < target{
                    l = mid + 1
                }else{
                    r = mid - 1
                }
            }
        }else{
            return false
        }
    }
    return false
    
}