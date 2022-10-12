func largestPerimeter(nums []int) int {
    sort.Sort(sort.Reverse(sort.IntSlice(nums)))
    
    for i:=0;i<len(nums)-2;i++{
        if nums[i] + nums[i+1] > nums[i+2] && nums[i] + nums[i+2] > nums[i+1] && nums[i+1] + nums[i+2]> nums[i]{
            return nums[i] + nums[i+1] + nums[i+2]
        }
    }
    return 0
}