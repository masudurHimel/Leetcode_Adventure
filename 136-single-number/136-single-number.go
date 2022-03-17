func singleNumber(nums []int) int {
    res_dict := make(map[int]int)
    for i:=0;i<len(nums);i++{
        res_dict[nums[i]] = res_dict[nums[i]] + 1 
    }
    
    for k,v := range res_dict{
        if v == 1{
            return k
        }
    }
    
    return -1
}