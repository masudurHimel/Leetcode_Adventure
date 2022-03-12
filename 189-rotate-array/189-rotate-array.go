func rotate(nums []int, k int)  {
    if len(nums) < k{
        k = k%len(nums)
    }
    temp := make([]int, 0)
    sample := make([]int, 0)
    temp = nums[len(nums)-k:]
    sample = nums[:len(nums)-k]
    temp = append(temp, sample...)
    for i:=0;i<len(nums);i++{
        nums[i] = temp[i]
    }
}