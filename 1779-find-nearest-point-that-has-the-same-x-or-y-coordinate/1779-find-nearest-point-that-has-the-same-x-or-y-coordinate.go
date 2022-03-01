func nearestValidPoint(x int, y int, points [][]int) int {
    res := -1
    min_dist := float64(99999)
    var tmp float64
    for i:=0;i<len(points);i++{
        if points[i][0] == x || points[i][1] == y{
            tmp = math.Abs(float64(x-points[i][0])) + math.Abs(float64(y-points[i][1]))
            if tmp < min_dist{
                res = i
                min_dist = tmp
            }
        } 
    }
    return res
}