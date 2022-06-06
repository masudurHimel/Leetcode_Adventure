func productExceptSelf(nums []int) []int {
    x := make([]int, len(nums))
    
    x[0] = 1
    
    for i:=1;i<len(nums);i++{
        x[i] = x[i-1] * nums[i-1]
    }
    
    temp := nums[len(nums)-1]
    
    for i:=len(nums)-2;i>=0;i--{
        x[i] *= temp
        temp *= nums[i]
    }
    
    return x
}


