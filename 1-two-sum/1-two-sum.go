func twoSum(nums []int, target int) []int {
    resMap := make(map[int]int)
    res := []int{-1,-1}
    
    for i,v := range nums{
        if _, e := resMap[v]; e == false{
            resMap[target-v] = i
        }else{
            res[0], res[1] = resMap[v], i
            return res
        }
    }
    
    return res
    
}