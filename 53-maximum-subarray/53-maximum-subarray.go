func maxSubArray(nums []int) int {
    max_res := nums[0]
    res := make([]int, len(nums))
    res[0] = nums[0]
    var temp int
    
    for i:=1;i<len(nums);i++{
        temp = nums[i] + res[i-1]
        if temp > nums[i]{
            res[i] = temp
        }else{
            res[i] = nums[i]
        }
        
        if max_res < res[i]{
            max_res = res[i]
        }
    }
    return max_res
}