func rotate(nums []int, k int)  {
    k = k%len(nums)
    temp := append(nums[len(nums)-k:], nums[:len(nums)-k]...)
    for i:=0;i<len(nums);i++{
        nums[i] = temp[i]
    }
}