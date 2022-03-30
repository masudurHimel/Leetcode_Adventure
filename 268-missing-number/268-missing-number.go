func missingNumber(nums []int) int {
    total_sum := ((len(nums))*(len(nums)+1))/2
    for _,v := range nums{
        total_sum -= v
    }
    return total_sum
}