func productExceptSelf(nums []int) []int {
    x := make([]int, len(nums))
    y := make([]int, len(nums))
    
    x[0], y[len(nums)-1] = 1, 1
    
    for i:=1;i<len(nums);i++{
        x[i] = x[i-1] * nums[i-1]
    }
    
    for i:=len(nums)-2;i>=0;i--{
        y[i] = y[i+1] * nums[i+1]
    }
    
    for i:=0;i<len(nums);i++{
        x[i] = x[i] * y[i]
    }
    
    return x
}


