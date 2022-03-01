func arraySign(nums []int) int {
    neg_flag := 1
    for i:=0;i<len(nums);i++{
        if nums[i] == 0{
            return 0
        } else if nums[i] < 0{
            neg_flag *= -1
        }
    }
    
    return neg_flag
}