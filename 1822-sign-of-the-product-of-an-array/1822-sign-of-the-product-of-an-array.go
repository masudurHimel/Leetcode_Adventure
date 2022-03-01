func arraySign(nums []int) int {
    neg_counter := 0
    for i:=0;i<len(nums);i++{
        if nums[i] == 0{
            return 0
        } else if nums[i] < 0{
            neg_counter++
        }
    }
    if neg_counter % 2 != 0{
        return -1
    }
    
    return 1
}